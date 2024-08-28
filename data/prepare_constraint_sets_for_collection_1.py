import json
import numpy as np
from data.utilities import generate_hard_constraints, generate_noisy_constraints


def prepare_constraint_sets_for_collection_1():

    # We noticed that the constraint sets for the data sets Iris and Wine contain ML and CL constraints that do not
    # comply with the ground truth. For these two data sets, we generated our own constraint sets according to the
    # procedure described in (Gonz´alez-Almagro et al., 2020).
    datasets = ['appendicitis',
                'breast_cancer',
                'bupa',
                'circles',
                'ecoli',
                'glass',
                'haberman',
                'hayes-roth',
                'heart',
                'ionosphere',
                'led7digit',
                'monk-2',
                'moons',
                'movement_libras',
                'newthyroid',
                'saheart',
                'sonar',
                'soybean',
                'spectfheart',
                'spiral',
                'tae',
                'vehicle',
                'zoo']

    parameters = [0.05, 0.10, 0.15, 0.2]
    path = r"data/raw data/COL1/constraint sets/"

    for dataset in datasets:
        for param_nf in parameters:
            filename = dataset + '(' + '{:.2f}'.format(param_nf) + ').txt'
            constraint_matrix = np.triu(np.loadtxt(path + filename), k=1)
            must_link = np.nonzero(constraint_matrix == 1)
            must_link_pairs = list(zip(must_link[0].tolist(), must_link[1].tolist()))
            cannot_link = np.nonzero(constraint_matrix == -1)
            cannot_link_pairs = list(zip(cannot_link[0].tolist(), cannot_link[1].tolist()))

            constraints = {'ml': must_link_pairs, 'cl': cannot_link_pairs, 'sml': [], 'scl': [], 'sml_proba': [],
                           'scl_proba': []}

            file_name = ('data/processed data/COL1/constraint sets/' + dataset + '_constraints_'
                         + '{:g}'.format(param_nf) + '.json'.format(param_nf))
            with open(file_name, 'w') as fp:
                json.dump(constraints, fp)

    # Generate constraints for data sets iris and wine
    for dataset in ['iris', 'wine']:
        for param_nf in parameters:
            generate_hard_constraints('COL1', dataset, param_nf, 24)


def generate_noisy_constraint_sets_for_collection_1(datasets):

    for dataset in datasets:
        for param_nf in [0.05, 0.1, 0.15, 0.2]:
            for lower_bound in [0.5, 0.6, 0.7, 0.8, 0.9, 1]:
                generate_noisy_constraints('COL1', dataset, param_nf, 24, lower_bound)


def generate_additional_constraint_sets_for_collection_1():

    datasets = ['appendicitis',
                'breast_cancer',
                'bupa',
                'circles',
                'ecoli',
                'glass',
                'haberman',
                'hayes-roth',
                'heart',
                'ionosphere',
                'led7digit',
                'monk-2',
                'moons',
                'movement_libras',
                'newthyroid',
                'saheart',
                'sonar',
                'soybean',
                'spectfheart',
                'spiral',
                'tae',
                'vehicle',
                'zoo']

    for dataset in datasets:
        for param_nf in [0]:
            generate_hard_constraints('COL1', dataset, param_nf, 24)

    print('Additional constraint sets for collection COL1 sucessfully generated.')