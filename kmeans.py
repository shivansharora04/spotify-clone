import random

# Step 1: Define a function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2  # Squared difference for each dimension
    return distance ** 0.5  # Return the square root of the sum of squared differences

# Step 2: Define the K-Means clustering algorithm
def kmeans(X, k, max_iters=100, tol=1e-4):
    # Randomly initialize centroids by selecting 'k' random points from the dataset
    centroids = random.sample(X, k)
    print("Initial Centroids:", centroids)

    for _ in range(max_iters):
        # Step 3: Assign each point to the nearest centroid
        clusters = [[] for _ in range(k)]  # Create k empty clusters

        for point in X:
            # Calculate the distance of the point to each centroid and find the closest centroid
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid_idx = distances.index(min(distances))  # Get the index of the closest centroid
            clusters[closest_centroid_idx].append(point)  # Assign the point to the corresponding cluster
        
        # Step 4: Update centroids
        new_centroids = []
        for cluster in clusters:
            # Calculate the mean of each cluster (average of points in that cluster)
            new_centroids.append([sum(dim)/len(dim) for dim in zip(*cluster)])  # Mean for each dimension
        
        print("\nUpdated Centroids:", new_centroids)

        # Check for convergence (if the centroids don't change much, break the loop)
        diff = sum(euclidean_distance(c, n) for c, n in zip(centroids, new_centroids))  # Total change in centroids
        if diff < tol:  # If change is less than tolerance, break the loop
            print("Convergence reached!")
            break
        
        centroids = new_centroids  # Update centroids for the next iteration

    return centroids, clusters  # Return final centroids and clusters

# Step 5: Test the K-Means algorithm with sample data
if __name__ == "__main__":
    # Sample dataset (2D points)
    X = [
        [1, 2], [1, 4], [1, 0],
        [10, 2], [10, 4], [10, 0]
    ]
    
    k = 2  # Number of clusters
    centroids, clusters = kmeans(X, k)

    # Print final centroids and cluster assignments
    print("\nFinal Centroids:", centroids)
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}: {cluster}")