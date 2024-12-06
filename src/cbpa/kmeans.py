#This file will contain pre-defined ml functions; to be called by main.py for comparison

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
import pandas as pd
import numpy as np

def sklearn_ml_kmeans(df, original_data, k):
    df = df.drop('Customer ID', axis='columns')
    # Apply K-Means clustering (e.g., 2 clusters)
    kmeans = KMeans(n_clusters=k)

    
    #make sure processed data was clustered
    #print(df)
    cluster_labels = kmeans.fit_predict(df)
    #print(cluster_labels)
    df['Cluster'] = cluster_labels
    original_data['Cluster'] = cluster_labels

    sil_score = silhouette_score(df, cluster_labels)
    db_score = davies_bouldin_score(df, cluster_labels)

    cluster_dfs = [original_data[original_data['Cluster'] == i] for i in range(kmeans.n_clusters)]

    return(cluster_dfs, sil_score, db_score)

if __name__ == '__main__':
    processed_data = pd.read_csv('../../data/processed/test_cluster_data_processed.csv')
    #df = pd.read_csv('../../data/processed/shopping_trends_processed.csv')

    #For testing
    original_data = pd.read_csv('../../data/original/test_cluster_data/test_cluster_data.csv')
    original_data = original_data.drop('Cluster_Label', axis='columns')
    print(sklearn_ml_kmeans(processed_data, original_data, 2))

