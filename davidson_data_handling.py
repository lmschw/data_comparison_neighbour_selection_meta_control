import h5py

filename = "c:/Users/rohan/Downloads/10-fish-0105/0105/0105_000_fov.h5"

h5 = h5py.File(filename,'r')

print(h5["fields"].keys())
h5.close()