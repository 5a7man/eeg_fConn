# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:53:29 2022

@author: Muhammad Salman Kabir
@purpose: Functions to do band pass filteration andcomputing connectivity matrix
          and/or connectivity vector
@regarding: Functional connectivity anaylsis    
"""

## Importing necassary libraries
import numpy as np
import scipy.signal as ss

def filteration(data,f_min,f_max,fs):
    """
    Parameters
    ----------
    data : Array of float
        DESCRIPTION. EEG data
    f_min : float
        DESCRIPTION. Low pass frequency of band pass filter given in hertz
    f_max : TYPE: float
        DESCRIPTION. High pass frequency of band pass filter given in hertz
    fs : TYPE: float
        DESCRIPTION. Sampling frequency of data given in hertz

    Returns 
    -------
    TYPE: Array of float
        DESCRIPTION. Filtered EEG data

    """
    print("Filteration in process.....")
    
    # filter design
    sos = ss.butter(N=10,Wn=[f_min,f_max],btype='bandpass',
                    analog=False,output='sos',fs=fs)

    # returning filter data
    print("Filteration done!")
    return ss.sosfilt(sos,data)


def plv_connectivity(sensors,data):
    """
    Parameters
    ----------
    sensors : INT
        DESCRIPTION. No of sensors used for capturing EEG
    data : Array of float 
        DESCRIPTION. EEG Data
    
    Returns
    -------
    connectivity_matrix : Matrix of float
        DESCRIPTION. PLV connectivity matrix
    connectivity_vector : Vector of flaot 
        DESCRIPTION. PLV connectivity vector

    """
    print("PLV in process.....")
    
    # Predefining connectivity matrix
    connectivity_matrix = np.zeros([sensors,sensors],dtype=float)
    
    # Computing hilbert transform
    data_points = data.shape[-1]
    data_hilbert = np.imag(ss.hilbert(data))
    phase = np.arctan(data_hilbert/data)
    
    # Computing connectivity matrix 
    for i in range(sensors):
        for k in range(sensors):
            connectivity_matrix[i,k] = np.abs(np.sum(np.exp(1j*(phase[i,:]-phase[k,:]))))/data_points
            
    # Computing connectivity vector
    connectivity_vector = connectivity_matrix[np.triu_indices(connectivity_matrix.shape[0],k=1)] 
      
    # returning connectivity matrix and vector
    print("PLV done!")
    return connectivity_matrix, connectivity_vector
            
def pli_connectivity(sensors,data):
    """
    Parameters
    ----------
    sensors : INT
        DESCRIPTION. No of sensors used for capturing EEG
    data : Array of float 
        DESCRIPTION. EEG Data

    Returns
    -------
    connectivity_matrix : Matrix of float
        DESCRIPTION. PLI connectivity matrix
    connectivity_vector : Vector of flaot 
        DESCRIPTION. PLI connectivity vector

    """
    print("PLI in process.....")
    # Predefining connectivity matrix
    connectivity_matrix = np.zeros([sensors,sensors],dtype=float)
    
    # Computing hilbert transform
    data_points = data.shape[-1]
    data_hilbert = np.imag(ss.hilbert(data))
    phase = np.arctan(data_hilbert/data)
    
    # Computing connectivity matrix
    for i in range(sensors):
        for k in range(sensors):
            connectivity_matrix[i,k] = np.abs(np.sum(np.sign(phase[i,:]-phase[k,:])))/data_points
    
    # Computing connectivity vector
    connectivity_vector = connectivity_matrix[np.triu_indices(connectivity_matrix.shape[0],k=1)] 
    
    # returning connectivity matrix and vector
    print("PLI done!")
    return connectivity_matrix, connectivity_vector


def ccf_connectivity(sensors,data):
    """
    Parameters
    ----------
    sensors : INT
        DESCRIPTION. No of sensors used for capturing EEG
    data : Array of float 
        DESCRIPTION. EEG Data

    Returns
    -------
    connectivity_matrix : Matrix of float
        DESCRIPTION. CCF connectivity matrix
    connectivity_vector : Vector of flaot 
        DESCRIPTION. CCF connectivity vector

    """
    print("CCF in process.....")
    
    # Predefining connectivity matrix
    connectivity_matrix = np.zeros([sensors,sensors],dtype=float)
    
    # Computing cross correlation
    for i in range(sensors):
        for k in range(sensors):
            temp = np.corrcoef(data[i,:],data[k,:])
            connectivity_matrix[i,k] = temp[0][1]
    
    # Computing connectvity vector
    connectivity_vector = connectivity_matrix[np.triu_indices(connectivity_matrix.shape[0],k=1)] 
    
    # Returning connectivity matrix and connectivity vector
    print("CCF done!")
    return connectivity_matrix, connectivity_vector


def coh_connectivity(sensors,data,f_min,f_max,fs):
    """
    Parameters
    ----------
    sensors : INT
        DESCRIPTION. No of sensors used for capturing EEG
    data : Array of float 
        DESCRIPTION. EEG Data
    
    Returns
    -------
    connectivity_matrix : Matrix of float
        DESCRIPTION. COH connectivity matrix
    connectivity_vector : Vector of flaot 
        DESCRIPTION. COH connectivity vector

    """
    print("COH in process.....")
    
    # Predefinig connectivity matrix
    connectivity_matrix = np.zeros([sensors,sensors],dtype=float)
    
    # Computing coherence 
    for i in range(sensors):
        for k in range(sensors):
            f, Cxy = ss.coherence(data[i,:],data[k,:],fs = fs)
            connectivity_matrix[i,k] = np.mean(Cxy[np.where((f>=f_min) & (f<=f_max))])
    
    # Computing connectivity vector
    connectivity_vector = connectivity_matrix[np.triu_indices(connectivity_matrix.shape[0],k=1)] 
    
    # returning connectivity matrix and/or vector
    print("COH done!")
    return connectivity_matrix, connectivity_vector

            
    