import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

# Load first 6 samples
X = load_iris().data[:6]

# Single Linkage Dendrogram
plt.figure()
dendrogram(linkage(X, method='single'))
plt.title("Single Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# Complete Linkage Dendrogram
plt.figure()
dendrogram(linkage(X, method='complete'))
plt.title("Complete Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()