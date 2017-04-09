# CSV to Images
import pandas as pd
%matplotlib inline 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('https://query.data.world/s/31xw9dudtdhgukx55rjvaz1ur',header=None)
X  = df.values.reshape(128,128,169)[:,:,1::21]
TR = [508.2336, 1000,1500,2500,3500,4500,5500,6500]