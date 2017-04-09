#define variables
rows = 128
cols = 128
slices = 21
TR = [508.2336, 1000,1500,2500,3500,4500,5500,6500]

# load data from data.world/julio/learn-quantitative-mri 
import pandas as pd
df = pd.read_csv('https://query.data.world/s/31xdudtdhgukx55rjvaz1ur',header=None)
T1data  = df.values[:,1::slices]

# convert first slice to an image
import matplotlib.pyplot as plt
plt.figure(1)
I = T1data[:,0].reshape(rows,cols)
# plot
plt.imshow(I,cmap='nipy_spectral'); plt.colorbar()
plt.title("First Image of the data set")

# create binary mask for noise using signal to noise ratio
from numpy import std
SNR = 20
noise_mask = (I / std(T1data[0,:])) >= SNR
# plot
plt.figure(2)
plt.imshow(noise_mask,cmap='hot'); plt.colorbar()
plt.title("Noise mask")
# noise mask to vector
noise_filter = noise_mask.reshape(rows*cols)

# Filter voxels with only the desired SNR.
T1data_2process = T1data[noise_filter,:]

# normalize to maximum
L = np.array(list((map(lambda x: x/x[-1],T1data_2process))))
plt.plot(TR,L);

m = map(lambda x: x/x[-1], T1data_2process[0::700,:])
m = np.array(list(m))
plt.plot(TR,m);

