import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("ToyotaCorolla.csv")
x=data['KM']
y=data['Weight']
z=data['Price']
plt.tricontourf(x,y,z,levels=20,cmap="jet")
plt.colorbar(label='price')
plt.title("contour")
plt.show()