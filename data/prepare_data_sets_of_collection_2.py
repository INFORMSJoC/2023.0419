# %% Load packages
import pandas as pd
from sklearn.datasets import make_blobs
from data.utilities import preprocess_and_export


def prepare_collection_2():
    n_samples = 300
    ls_clusters = [10, 20, 50]
    cluster_stds = [1, 2, 3, 4, 5]
    center_box = (-20, 20)

    for cluster_std in cluster_stds:
        for n_clusters in ls_clusters:

            # Define name of data set
            name = 'synthetic_n{}_d2_k{}_s{:d}'.format(n_samples, n_clusters, int(cluster_std*10))

            # Create data set
            X, y = make_blobs(n_samples=n_samples, n_features=2, centers=n_clusters, random_state=24,
                              cluster_std=cluster_std, center_box=center_box)

            # Create DataFrame
            df = pd.DataFrame(X)
            df['class'] = y

            # Preprocess and export
            preprocess_and_export(df, name, 'COL2')

    print('Data sets from collection COL2 sucessfully generated.')
