import pandas as pd
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Parameters for synthetic data
n_samples = 1000  # Total number of data points
n_features = 2    # Number of features (dimensions)
n_clusters = 3    # Number of clusters
cluster_std = 4 # Standard deviation of clusters (controls overlap, lower number less overlap)

# Generate synthetic data with clusters
data, labels = make_blobs(n_samples=n_samples, centers=n_clusters, n_features=n_features, cluster_std=cluster_std, center_box=(0, 100))

print(data)

if n_features == 2:
    # Convert to a DataFrame for easier handling
    df = pd.DataFrame(data, columns=['Feature_1', 'Feature_2'])
    df['Cluster_Label'] = labels  # Add cluster labels for reference

    df.plot(kind = 'scatter', x='Feature_1', y='Feature_2')
    plt.show()

# Output to a CSV file
output_file = "test_cluster_data.csv"
df.to_csv(output_file, index=False)

print(f"test data for clustering saved to {output_file}")
