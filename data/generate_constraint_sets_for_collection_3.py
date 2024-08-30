from data.utilities import generate_hard_constraints


def generate_constraint_sets_for_collection_3():
    ls_size = [500, 1000, 2000, 5000]
    ls_features = [2]
    ls_clusters = [2, 5, 10, 20, 50, 100]

    for n_samples in ls_size:
        for n_features in ls_features:
            for n_clusters in ls_clusters:

                # Define name of data set
                dataset = 'synthetic_n{}_d{}_k{}'.format(n_samples, n_features, n_clusters)

                for param_nf in [0, 0.05, 0.10, 0.15, 0.20]:
                    generate_hard_constraints('COL3', dataset, param_nf, 24)

    print('Constraint sets for collection COL3 sucessfully generated.')
