#This file will contain pre-defined ml functions; to be called by main.py for comparison

from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('../../data/processed/test_cluster_data_processed.csv')
#df = pd.read_csv('../../data/processed/shopping_trends_processed.csv')

clusters_with_ids = (pd.read_csv('../../data/original/test_cluster_data/test_cluster_data.csv'))['Cluster_Label']
print(clusters_with_ids)

print(df)

df = df.drop('Customer ID', axis='columns')

# Apply K-Means clustering (e.g., 2 clusters)
kmeans = KMeans(n_clusters=2)
df['Cluster'] = kmeans.fit_predict(df)

# Display the DataFrame with the cluster labels
print(df)

