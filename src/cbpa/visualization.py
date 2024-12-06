import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

def EDA_visualize_df(data, x, y, z, title):
    fig = px.scatter_3d(
        data,
        x=x,          # X-axis
        y=y,          # Y-axis
        z=z,          # Z-axis
        title=title
    )
    fig.show()

def EDA_visualize_df_with_clusters(data, x, y, z, title):
    fig = px.scatter_3d(
        data,
        x=x,          # X-axis
        y=y,          # Y-axis
        z=z,          # Z-axis
        title=title,
        color='Cluster',
        color_continuous_scale=px.colors.sequential.Inferno

    )
    fig.show()

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)
    

