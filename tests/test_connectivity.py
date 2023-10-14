from eeg_fConn import connectivity as con
import numpy as np

def setUp():
    # Set up common data or configurations for your tests
    global sensors, data, fs
    sensors = 10
    data = np.random.rand(sensors, 1000)  # Sample EEG data
    fs = 250  # Sample sampling frequency

def test_filteration():
    f_min = 5
    f_max = 20

    filtered_data = con.filteration(data, f_min, f_max, fs)

    # Perform assertions to check if filtered_data is as expected
    assert filtered_data.shape == data.shape

def test_plv_connectivity():
    connectivity_matrix, connectivity_vector = con.plv_connectivity(sensors, data)

    # Perform assertions to check if the PLV connectivity results are as expected
    assert connectivity_matrix.shape == (sensors, sensors)
    assert connectivity_vector.shape == (sensors * (sensors - 1) // 2,)

def test_pli_connectivity():
    connectivity_matrix, connectivity_vector = con.pli_connectivity(sensors, data)

    # Perform assertions to check if the PLI connectivity results are as expected
    assert connectivity_matrix.shape == (sensors, sensors)
    assert connectivity_vector.shape == (sensors * (sensors - 1) // 2,)

def test_ccf_connectivity():
    connectivity_matrix, connectivity_vector = con.ccf_connectivity(sensors, data)

    # Perform assertions to check if the CCF connectivity results are as expected
    assert connectivity_matrix.shape == (sensors, sensors)
    assert connectivity_vector.shape == (sensors * (sensors - 1) // 2,)

def test_coh_connectivity():
    f_min = 5
    f_max = 20

    connectivity_matrix, connectivity_vector = con.coh_connectivity(sensors, data, f_min, f_max, fs)

    # Perform assertions to check if the COH connectivity results are as expected
    assert connectivity_matrix.shape == (sensors, sensors)
    assert connectivity_vector.shape == (sensors * (sensors - 1) // 2,)

def test_icoh_connectivity():
    f_min = 5
    f_max = 20

    connectivity_matrix, connectivity_vector = con.icoh_connectivity(sensors, data, f_min, f_max, fs)

    # Perform assertions to check if the ICOH connectivity results are as expected
    assert connectivity_matrix.shape == (sensors, sensors)
    assert connectivity_vector.shape == (sensors * (sensors - 1) // 2,)

if __name__ == '__main__':
    setUp()
    test_filteration()
    test_plv_connectivity()
    test_pli_connectivity()
    test_ccf_connectivity()
    test_coh_connectivity()
    test_icoh_connectivity()
    print("All tests passed.")
