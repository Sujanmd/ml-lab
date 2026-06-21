import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("ToyotaCorolla.csv")
plt.title("box plot")
plt.boxplot([data['KM'],data['Price'],data['HP']])
plt.xticks([1,2,3],["km",'Price','hp'])
plt.show()