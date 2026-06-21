import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
data = pd.read_csv("glass.csv")

# Features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split dataset (70-30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Euclidean Distance
euclidean = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
euclidean.fit(X_train, y_train)

y_pred1 = euclidean.predict(X_test)

print("Euclidean Confusion Matrix:")
print(confusion_matrix(y_test, y_pred1))

print("\nEuclidean Accuracy:")
print(accuracy_score(y_test, y_pred1))

# Manhattan Distance
manhattan = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
manhattan.fit(X_train, y_train)

y_pred2 = manhattan.predict(X_test)

print("\nManhattan Confusion Matrix:")
print(confusion_matrix(y_test, y_pred2))

print("\nManhattan Accuracy:")
print(accuracy_score(y_test, y_pred2))