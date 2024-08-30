from data.utilities import generate_hard_constraints
import numpy as np


def generate_constraint_sets_for_collection_2():
    n_samples = 300
    ls_clusters = [10, 20, 50]
    cluster_stds = [1, 2, 3, 4, 5]

    for n_clusters in ls_clusters:
        for cluster_std in cluster_stds:

            # Define name of data set
            dataset = 'synthetic_n{}_d2_k{}_s{:d}'.format(n_samples, n_clusters, int(cluster_std * 10))

            for param_nf in np.arange(0.05, 0.55, 0.05):
                generate_hard_constraints('COL2', dataset, param_nf, 24)

    print('Constraint sets for collection COL2 sucessfully generated.')
