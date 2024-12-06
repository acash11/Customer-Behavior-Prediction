import pandas as pd
import numpy as np
import cbpa
from matplotlib import pyplot as plt

def apriori_comparison(df, list_of_clusters):
    #1. Run association rules on whole dataset
    #2 Identify most valuable cluster is cluster list
    #3. Run association rules on most valuable customer dataset, compare to whole dataset
    #list_of_clusters: List of all clusters found by clustering algorithm
    #df: entire dataset, not clustered
    def format_customer_behavior_data(dataset):
        age_bins = [0, 19, 39, 59, float('inf')]  # Define the bin edges
        age_labels = ['0-19', '20-39', '40-59', '60+']  # Define the category labels
        review_bins = [0, 1, 2, 3, 4, float('inf')]  # Define the bin edges
        review_labels = ['0-1', '1-2', '2-3', '3-4', '4+']  # Define the category labels

        dataset = dataset.drop(columns=['Customer ID', 'Purchase Amount (USD)', 'Previous Purchases', 'Frequency of Purchases (per year)', 'Cluster'])
        dataset['Age'] = pd.cut(dataset['Age'], bins=age_bins, labels=age_labels, right=True)
        dataset['Review Rating'] = pd.cut(dataset['Review Rating'], bins=review_bins, labels=review_labels, right=True)
        dataset['Subscription Status'] = dataset['Subscription Status'] + 'Subscr'
        dataset['Discount Applied'] = dataset['Discount Applied'] + 'Disco'
        dataset['Promo Code Used'] = dataset['Promo Code Used'] + "Promo"
        return dataset
    
    # Function to calculate the sum of means for each DataFrame
    def sum_of_means(df):
        return df[['Purchase Amount (USD)', 'Frequency of Purchases (per year)', 'Previous Purchases']].mean().sum()
    
    # Find the index of the cluster with the highest sum of means; The most valuable cluster
    sums = [sum_of_means(d) for d in list_of_clusters]
    max_index = sums.index(max(sums))
    apriori_valuable_data = format_customer_behavior_data(list_of_clusters[max_index])
    apriori_all_data = format_customer_behavior_data(df)
    #print(apriori_all_data)
    #print(apriori_valuable_data)
    all_data = cbpa.apriori_algorithm([apriori_all_data], 0.2)
    valuable_data = cbpa.apriori_algorithm([apriori_valuable_data], 0.2)
    return {'all_data': all_data, 'valuable_data': valuable_data}

if __name__ == '__main__':

    #############################
    ###      GET DATA        ###
    ############################

    # processed_data = pd.read_csv('../data/processed/test_cluster_data_processed.csv')
    # original_data = pd.read_csv('../data/original/test_cluster_data/test_cluster_data.csv')

    processed_data = pd.read_csv('../data/processed/shopping_trends_processed.csv')
    original_data = pd.read_csv('../data/original/shopping_trends/shopping_trends.csv')
    frequency_mapping = {'Weekly': 52,'Fortnightly': 26,'Bi-Weekly': 26,'Monthly': 12,'Quarterly': 4,'Every 3 Months': 4,'Annually': 1}
    original_data['Frequency of Purchases (per year)'] = original_data['Frequency of Purchases'].map(frequency_mapping)
    original_data = original_data.drop('Frequency of Purchases', axis='columns')


    #############################
    ### SKLEARN KMEANS MODULE ###
    #############################

    #Exploratory Data Analysis
    cbpa.EDA_visualize_df(processed_data, processed_data['Purchase Amount (USD)'], processed_data['Frequency of Purchases (per year)'], processed_data['Previous Purchases'], "Data")

    #Use Siloutte Analysis to Perform K-means Clustering with the Optimal Argument for K
    max_siloutte = -2, 0

    #Search for k in this range
    for k in range(2, 5):
        cluster_list = cbpa.sklearn_ml_kmeans(processed_data, original_data, k)

        sil_score = cluster_list[1]
        #print("siloutte score:", cluster_list[1])
        if sil_score > max_siloutte[0]:
            max_siloutte = sil_score, k

    #Evaluate Clusters
    cluster_list = cbpa.sklearn_ml_kmeans(processed_data, original_data, max_siloutte[1])
    list_of_clusters = cluster_list[0]
    siloutte_score = cluster_list[1]
    davies_bouldin_score = cluster_list[2]
    #print("clusters", list_of_clusters)

    #Visualize Clusters
    df = pd.concat(list_of_clusters)
    processed_data['Cluster'] = df['Cluster']
    cbpa.EDA_visualize_df_with_clusters(processed_data, processed_data['Purchase Amount (USD)'], processed_data['Frequency of Purchases (per year)'], processed_data['Previous Purchases'], f"Siloutte Score: {siloutte_score} | Davies-Bouldin Score: {davies_bouldin_score}")

    #Find Association Rules in Whole dataset and most valuable cluster
    ars = apriori_comparison(df, list_of_clusters)
    print(ars['all_data'])
    print(ars['valuable_data'])
    ####
    ars['all_data']['fItemSets'].to_csv('output/freq_items_alldata.csv')
    ars['all_data']['AR'].to_csv('output/AR_alldata.csv')
    ars['valuable_data']['fItemSets'].to_csv('output/freq_items_valdata.csv')
    ars['valuable_data']['AR'].to_csv('output/AR_valdata.csv')
    

    #find overlapping item sets from both rules
    #find which ones have better support

    ####################################
    ### SKLEARN AGGLOMERATIVE MODULE ###
    ####################################

    # find best threshold

    max_silhouette = -2, 0
    besthold = 0

    for threshold in range(2, 10): #10 is arbitrary... just try numbers until you're happy
        cluster_list = cbpa.sklearn_ml_agglomerative(processed_data, original_data, threshold)
        sil_score = cluster_list[1]
        if sil_score > max_silhouette[0]:
            max_silhouette = sil_score, threshold
            besthold = threshold
            
    # evaluate clusters using best threshold
    cluster_list = cbpa.sklearn_ml_agglomerative(processed_data, original_data, besthold)
    list_of_clusters = cluster_list[0]
    siloutte_score = cluster_list[1]
    davies_bouldin_score = cluster_list[2]
    dendy = cluster_list[3]

    #Visualize the data
    plt.title("Hierarchical Clustering Dendrogram")
    # plot the top three levels of the dendrogram
    cbpa.plot_dendrogram(dendy, truncate_mode="level", p=5)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.ylabel("Distance points merged at.")
    plt.show()
    cbpa.plot_dendrogram(dendy)


    
