# Installation
```python
pip install eeg-fConn
```
# Usage
```python
import numpy as np
from eeg_fConn import connectivity as con

# dummy data
data = np.random.rand(10,200)

# filtering data
filtered_data = con.filteration(data=data, f_min=8, f_max=12, fs=250)

# pli connectivity
M,V = con.pli_connectivity(sensors=10,data=filtered_data)

# plv connectivity
M,V = con.plv_connectivity(sensors=10,data=filtered_data)

# ccf connectivity
M,V = con.ccf_connectivity(sensors=10,data=filtered_data)

# coh connectivity
M,V = con.coh_connectivity(sensors=10, data=data, f_min=8, f_max=12, fs=250)
```

Here _M_ and _V_ are _connectivity matrix_ and _connectivity vector_ respectively.