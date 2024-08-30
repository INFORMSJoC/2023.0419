# %% Load packages
import pandas as pd
from sklearn.datasets import make_blobs
from data.utilities import preprocess_and_export


def prepare_collection_3():
    ls_size = [500, 1000, 2000, 5000]
    ls_features = [2]
    ls_clusters = [2, 5, 10, 20, 50, 100]

    for n_samples in ls_size:
        for n_features in ls_features:
            for n_clusters in ls_clusters:

                # Define name of data set
                name = 'synthetic_n{}_d{}_k{}'.format(n_samples, n_features, n_clusters)

                # Create data set
                X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=24)

                # Create DataFrame
                df = pd.DataFrame(X)
                df['class'] = y

                # Preprocess and export
                preprocess_and_export(df, name, 'COL3')

    print('Data sets from collection COL3 sucessfully generated.')
