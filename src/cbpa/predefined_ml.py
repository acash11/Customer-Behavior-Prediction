#This file will contain pre-defined ml functions; to be called by main.py for comparison

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

df = pd.read_csv('../../data/processed/test_cluster_data_processed.csv')
#df = pd.read_csv('../../data/processed/shopping_trends_processed.csv')

real_clusters = (pd.read_csv('../../data/original/test_cluster_data/test_cluster_data.csv'))['Cluster_Label']
print(real_clusters)

#print(df)

def sklearn_ml_kmeans(df):
    df = df.drop('Customer ID', axis='columns')
    # Apply K-Means clustering (e.g., 2 clusters)
    kmeans = KMeans(n_clusters=2)
    df['Predicted Cluster'] = kmeans.fit_predict(df)

    return(df['Predicted Cluster'])

if __name__ == '__main__':
    p = sklearn_ml_kmeans(df)

    predicted_clusters = dict()
    for index, value in enumerate(p):
        if value not in predicted_clusters:
            predicted_clusters[value] = np.array(index)
        else:
            predicted_clusters[value] = np.append(predicted_clusters[value], index)
        
    print(predicted_clusters)
    print(real_clusters)

