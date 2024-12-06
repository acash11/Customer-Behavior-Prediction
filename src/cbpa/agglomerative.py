#This file will contain pre-defined ml functions; to be called by main.py for comparison

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
import pandas as pd


def sklearn_ml_agglomerative(df, original_data, threshold):
    df = df.drop('Customer ID', axis='columns')
    #apply agglomerative clustering - ward linkage method is the default
    agglomerative = AgglomerativeClustering(n_clusters=threshold, linkage='ward', compute_distances=True) #compute distances false by default. dont let it be
    agglomer = agglomerative.fit(df)
    
    #make sure processed data was clustered
    #print(df)
    cluster_labels = agglomerative.fit_predict(df)
    #print(cluster_labels)
    df['Cluster'] = cluster_labels
    original_data['Cluster'] = cluster_labels
    #print('ccc', df)

    sil_score = silhouette_score(df, cluster_labels)
    db_score = davies_bouldin_score(df, cluster_labels)

    #shunt into clusters
    cluster_dfs = [original_data[original_data['Cluster'] == i] for i in range(len(set(cluster_labels)))]

    return(cluster_dfs, sil_score, db_score, agglomer)

if __name__ == '__main__':
    processed_data = pd.read_csv('../../data/processed/test_cluster_data_processed.csv')
    #df = pd.read_csv('../../data/processed/shopping_trends_processed.csv')

    #For testing
    original_data = pd.read_csv('../../data/original/test_cluster_data/test_cluster_data.csv')
    original_data = original_data.drop('Cluster_Label', axis='columns')
    print(sklearn_ml_agglomerative(processed_data, original_data, 2))

