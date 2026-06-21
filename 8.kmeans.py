from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = load_iris().data

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

print("Labels:")
print(model.labels_)

print("\nCentroids:")
print(model.cluster_centers_)

plt.scatter(X[:,0], X[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0],
            model.cluster_centers_[:,1],
            marker='X', s=200)

plt.title("K-Means Clustering")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()