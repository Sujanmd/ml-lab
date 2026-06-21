import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n=100
data=pd.DataFrame({
    'X':np.random.normal(0,1,n),
    'Y':np.random.normal(0,1,n),
    'Category':np.random.choice(['A','B','C'],n)
    
})

plt.figure(figsize=(6,4))
sns.scatterplot(data=data,x='X',y='Y',hue='Category')
plt.title("2d plot")
plt.show()
