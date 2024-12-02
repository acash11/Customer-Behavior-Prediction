#Not real data: Test data for clustering and association algorithms

import pandas as pd
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import random

# Parameters for synthetic data
n_samples = 1000  # Total number of data points
n_features = 2    # Number of features (dimensions)
cluster_centers = [(25,25),(50,50)]    # Clusters
cluster_std = 6 # Standard deviation of clusters (controls overlap, lower number less overlap)

# Generate synthetic data with clusters
data, labels = make_blobs(n_samples=n_samples, centers=cluster_centers, n_features=n_features, cluster_std=cluster_std)

print(data)

if n_features != 2:
    print('n features not 2')
    exit()

# Convert to a DataFrame for easier handling
df = pd.DataFrame(data, columns=['time in store', 'money spent'])
df['Cluster_Label'] = labels  # Add cluster labels for reference

df.plot(kind = 'scatter', x='time in store', y='money spent')
plt.show()

#Generate categorical attributes to test association
states = ['Ohio', 'Michigan', 'Pennsylvania', 'Virginia', 'Indiana', 'Kentucky', 'West Virginia']
random_states = [random.choice(states) for _ in range(1000)]
#print(random_states)
df['Home State'] = random_states
#print(df)

hobbies = []
some_hobbies = ["cooking", "traveling", "reading", "writing", "sports", "art", "music", "food"]
for index, row in df.iterrows():
    if row['time in store'] > 37 and random.randrange(101) < 90:
        hobbies.append('sports')
    else:
        hobbies.append(random.choice(some_hobbies))

#print(hobbies)
df["Hobby"] = hobbies
    
print(df)

# Output to a CSV file
output_file = "test_cluster_data.csv"
df.to_csv(output_file, index=False)

print(f"test data for clustering saved to {output_file}")
