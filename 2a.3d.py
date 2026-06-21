import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('ToyotaCorolla.csv')
x=data['KM']
y=data['Doors']
z=data['Price']
ax=plt.axes(projection='3d')
ax.plot_trisurf(x,y,z,cmap="jet")
ax.set_title("3d plot")
plt.show()