from eeg_fConn import connectivity
import numpy as np
def test_pli():
    M,V = connectivity.plv_connectivity(5, np.ones([5,5]))
    assert sum(sum(M))==25.0