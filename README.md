# Implemented Programs(22CS67L) 

1. Scatter Plot Visualization and Hill Climbing Algorithm
2. 3D Surface Plot and Best First Search (BFS)
3. Contour Plot and A* Search Algorithm
4. Heat Map Visualization and Min-Max Algorithm
5. Box Plot and Alpha-Beta Pruning
6. Naive Bayes Classifier using Titanic Dataset
7. K-Nearest Neighbors (KNN) using Glass Dataset
8. K-Means Clustering using Iris Dataset
9. Agglomerative Hierarchical Clustering
10. Principal Component Analysis (PCA)
11. Linear Discriminant Analysis (LDA)
12. Single Layer Perceptron for AND and OR Gates

---

## Viva Questions & Answers

### 1. Scatter Plot Visualization
* **Q1: What is a scatter plot, and when is it used?**
  * **A:** A scatter plot is a 2D data visualization that uses dots to represent values for two different variables. It is primarily used to detect relationships, correlations, and distributions between two continuous numerical variables.
* **Q2: How do you interpret correlation in a scatter plot?**
  * **A:** If points trend upward from left to right, it indicates a **positive correlation**. If they trend downward from left to right, it shows a **negative correlation**. A random, cloud-like distribution indicates **no correlation**.

### 2. Hill Climbing Algorithm
* **Q1: What is the Hill Climbing algorithm?**
  * **A:** Hill Climbing is a local search mathematical optimization technique. It starts with an arbitrary solution and iteratively makes incremental changes. If a change produces a better solution, it is adopted. This process repeats until no further improvements can be found.
* **Q2: What are the main drawbacks of the Hill Climbing algorithm?**
  * **A:** 
    * **Local Maxima:** Getting stuck at a peak that is higher than its neighbors but lower than the global maximum.
    * **Plateaus:** Flat regions where all neighboring states have the same value, making it impossible to determine the best direction.
    * **Ridges:** Sloping regions where the local search oscillates or gets stuck due to orthogonal move limitations.

### 3. 3D Surface Plot
* **Q1: What is a 3D surface plot, and what variables does it depict?**
  * **A:** A 3D surface plot is used to visualize the relationship among three continuous variables ($X$, $Y$, and $Z$). It plots a functional relationship $z = f(x, y)$ as a colored, continuous three-dimensional surface.
* **Q2: How does a wireframe plot differ from a surface plot in visualization libraries like Matplotlib?**
  * **A:** A wireframe plot draws only the grid lines connecting the data points in 3D space, leaving the regions between them transparent. A surface plot fills the polygons between the grid lines with color, often using a colormap to signify the $Z$-axis values (height).

### 4. Best First Search (BFS)
* **Q1: What is Best First Search (Informed Search)?**
  * **A:** Best First Search is an informed search algorithm that selects the next node to expand based on an evaluation function $f(n) = h(n)$, where $h(n)$ is a heuristic estimating the cost from the current node $n$ to the goal. It uses a priority queue to explore the most promising paths first.
* **Q2: How does Best First Search differ from standard Breadth-First Search (BFS)?**
  * **A:** Standard Breadth-First Search is *uninformed* (blind) and expands nodes level-by-level using a FIFO queue. Best First Search is *informed* (heuristic-guided) and uses a priority queue to explore nodes that appear closest to the goal, regardless of depth.

### 5. Contour Plot
* **Q1: What is a contour plot, and what do the contour lines represent?**
  * **A:** A contour plot is a technique used to represent a 3D surface on a 2D plane. Each line (contour) represents a constant value of the dependent variable $z = f(x,y)$. Closer contour lines indicate a steeper slope.
* **Q2: What is the difference between `contour()` and `contourf()` in Python's Matplotlib?**
  * **A:** `contour()` draws only the contour lines (isolines), whereas `contourf()` draws filled contour regions with solid colors or gradients between the lines.

### 6. A* Search Algorithm
* **Q1: How does the A* search algorithm select nodes for expansion?**
  * **A:** A* selects nodes by minimizing $f(n) = g(n) + h(n)$, where:
    * $g(n)$ is the exact cost to reach node $n$ from the start node.
    * $h(n)$ is the heuristic estimated cost to reach the goal from node $n$.
* **Q2: What does it mean for a heuristic in A* to be "admissible" and "consistent"?**
  * **A:** 
    * **Admissible:** The heuristic never overestimates the actual cost to reach the goal ($h(n) \le h^*(n)$).
    * **Consistent (Monotonic):** The heuristic satisfies the triangle inequality: $h(n) \le c(n, a, n') + h(n')$, where $c(n, a, n')$ is the cost of going from $n$ to $n'$ via action $a$. Consistency guarantees that A* finds the optimal path without re-evaluating closed nodes.

### 7. Heat Map Visualization
* **Q1: What is a heatmap, and when is it useful in Machine Learning?**
  * **A:** A heatmap is a graphical representation of data where values in a matrix are represented as colors. In Machine Learning, it is extremely useful for visualizing correlation matrices, confusion matrices, and missing values.
* **Q2: Which Python library and function are most commonly used to plot heatmaps?**
  * **A:** Seaborn's `sns.heatmap()` function is the standard tool, typically styled using Matplotlib's colormaps.

### 8. Min-Max Algorithm
* **Q1: What is the Min-Max algorithm, and where is it applied?**
  * **A:** Min-Max is a recursive decision-making algorithm used in game theory and AI for two-player, zero-sum, turn-based games (e.g., Tic-Tac-Toe, Chess). It determines the optimal move by assuming that the player maximizes their score while the opponent minimizes it.
* **Q2: How does the minimax value propagate through the game tree?**
  * **A:** It propagates bottom-up from leaf nodes. At "Max" levels, the node takes the maximum value of its children. At "Min" levels, the node takes the minimum value of its children.

### 9. Box Plot
* **Q1: What are the key statistical components of a box plot (5-number summary)?**
  * **A:**
    * **Minimum:** Lowest data point excluding outliers.
    * **First Quartile ($Q1$ / 25th percentile):** Median of the lower half of the data.
    * **Median ($Q2$ / 50th percentile):** The middle value of the dataset.
    * **Third Quartile ($Q3$ / 75th percentile):** Median of the upper half of the data.
    * **Maximum:** Highest data point excluding outliers.
* **Q2: How are outliers defined mathematically in a box plot?**
  * **A:** Outliers are points that fall beyond $1.5 \times \text{IQR}$ (Interquartile Range, where $\text{IQR} = Q3 - Q1$) from the quartiles:
    * Below $Q1 - 1.5 \times \text{IQR}$
    * Above $Q3 + 1.5 \times \text{IQR}$

### 10. Alpha-Beta Pruning
* **Q1: What is Alpha-Beta pruning, and what is its primary benefit?**
  * **A:** Alpha-Beta pruning is an optimization technique for the minimax algorithm. It avoids searching branches of the game tree that cannot influence the final decision, significantly reducing search time without changing the minimax output.
* **Q2: What do the parameters $\alpha$ and $\beta$ represent?**
  * **A:** 
    * **$\alpha$:** The best (highest) value that the Max player can guarantee so far.
    * **$\beta$:** The best (lowest) value that the Min player can guarantee so far. 
    * **Pruning Condition:** A branch is pruned when $\alpha \ge \beta$.

### 11. Naive Bayes Classifier (Titanic Dataset)
* **Q1: Why is the Naive Bayes classifier called "naive"?**
  * **A:** It is called "naive" because it assumes that all features in the dataset are conditionally independent of each other given the class label, which is rarely true in practice.
* **Q2: What is the underlying formula of Bayes' Theorem used by the classifier?**
  * **A:** $P(y|x_1, \dots, x_n) = \frac{P(x_1, \dots, x_n|y) \cdot P(y)}{P(x_1, \dots, x_n)}$. Using the independence assumption, it simplifies to:
    $$P(y|x_1, \dots, x_n) \propto P(y) \prod_{i=1}^n P(x_i|y)$$
    The class with the highest probability is predicted.

### 12. K-Nearest Neighbors (KNN) (Glass Dataset)
* **Q1: How does the KNN algorithm classify a new data point?**
  * **A:** KNN is a instance-based (lazy) learner. It calculates the distance (typically Euclidean) from the new point to all training data points, finds the $K$ closest points, and assigns the class label by majority vote.
* **Q2: How does the value of $K$ affect the bias and variance of the model?**
  * **A:** 
    * **Low $K$ (e.g., $K=1$):** Low bias, high variance. The decision boundary is highly complex, making it sensitive to noise and prone to overfitting.
    * **High $K$:** High bias, low variance. The decision boundary is smoother, but it may underfit by averaging out small/rare classes.

### 13. K-Means Clustering (Iris Dataset)
* **Q1: What are the iterative steps of the K-Means clustering algorithm?**
  * **A:** 
    1. Initialize $K$ cluster centroids randomly.
    2. Assign each data point to the closest centroid (based on Euclidean distance).
    3. Update the centroid positions by calculating the mean of all points assigned to each cluster.
    4. Repeat steps 2 and 3 until centroids stabilize (convergence) or max iterations are reached.
* **Q2: What are the standard methods to determine the optimal number of clusters $K$?**
  * **A:** 
    * **Elbow Method:** Plotting Within-Cluster Sum of Squares (WCSS / Inertia) vs. $K$ and identifying the "elbow" point where the rate of decrease sharpens.
    * **Silhouette Score:** Calculating the silhouette width of clustering outputs to evaluate cluster separation and cohesion.

### 14. Agglomerative Hierarchical Clustering
* **Q1: How does Agglomerative Hierarchical Clustering work?**
  * **A:** It is a bottom-up clustering approach. It starts by treating each data point as a single cluster and successively merges the closest pairs of clusters until only a single cluster remains, constructing a tree-like diagram called a **dendrogram**.
* **Q2: Explain the common linkage criteria (Single, Complete, Average, Ward's).**
  * **A:** 
    * **Single Linkage:** Distance between the closest points of two clusters.
    * **Complete Linkage:** Distance between the farthest points of two clusters.
    * **Average Linkage:** Average distance between all pairs of points in two clusters.
    * **Ward's Linkage:** Minimizes the total within-cluster variance when merging.

### 15. Principal Component Analysis (PCA)
* **Q1: What is PCA, and is it a supervised or unsupervised technique?**
  * **A:** PCA is an unsupervised dimensionality reduction technique. It projects high-dimensional data onto a lower-dimensional orthogonal space (principal components) that maximizes the variance of the projected data.
* **Q2: What is the relationship between Principal Components and covariance?**
  * **A:** Principal components are the eigenvectors of the data's covariance matrix, and their corresponding eigenvalues represent the amount of variance explained along those components.

### 16. Linear Discriminant Analysis (LDA)
* **Q1: What is the key difference between PCA and LDA?**
  * **A:** 
    * **PCA** is unsupervised; it ignores class labels and finds axes that maximize data variance.
    * **LDA** is supervised; it uses class labels to find axes that maximize between-class variance relative to within-class variance, ensuring optimal class separation.
* **Q2: What is the maximum number of components that LDA can generate?**
  * **A:** LDA is mathematically restricted to a maximum of $C - 1$ components, where $C$ is the number of classes in the dataset.

### 17. Single Layer Perceptron
* **Q1: What is a Single Layer Perceptron, and what is its decision rule?**
  * **A:** A perceptron is the simplest form of artificial neural network used for binary classification. It calculates a weighted sum of inputs plus a bias: $z = \sum (w_i \cdot x_i) + b$, and passes it through a step function (e.g., outputs $1$ if $z \ge 0$, and $0$ otherwise).
* **Q2: Why can a Single Layer Perceptron solve AND/OR gates but not the XOR gate?**
  * **A:** A single-layer perceptron can only learn linear decision boundaries (linearly separable functions). AND and OR gates are linearly separable (can be split by a single line), whereas XOR is non-linearly separable and requires a Multilayer Perceptron (MLP) or hidden layers to solve.
