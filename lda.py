import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load Iris Datasets
iris = load_iris()

X = iris.data
y = iris.target

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

# Output
print("Original Shape:", X.shape)
print("Transformed Shape:", X_lda.shape)

# Visualization
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y)

plt.title("LDA on Iris Dataset")
plt.xlabel("LD1")
plt.ylabel("LD2")

plt.show()