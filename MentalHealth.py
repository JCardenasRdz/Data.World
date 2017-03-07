import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Genhance680_37C_72pH.xlsx')
df.head(1)
df.set_index('Wavelength',inplace=True)

max = df['10µM'].loc[680]
ec = 1e5
df = df.apply(lambda x: (x/max) * ec )
plt.figure(dpi=600);
df.plot()
plt.xlim(xmin=450,xmax=950)
plt.ylabel('Molar Extinction Coefficient',fontsize=15)
plt.xlabel('Wavelength',fontsize=15)




