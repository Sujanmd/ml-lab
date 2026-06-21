import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

# Load Iris Dataset
X = load_iris().data

# Single Linkage
single = linkage(X, method='single')

plt.figure()
dendrogram(single)

plt.title("Single Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# Complete Linkage
complete = linkage(X, method='complete')

plt.figure()
dendrogram(complete)

plt.title("Complete Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()