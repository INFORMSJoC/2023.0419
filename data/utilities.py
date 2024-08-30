import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def get_data_from_dat_file(dataset, folder):
    # Read raw data
    f = open('data/raw data/' + folder + '/' + dataset + '.dat')
    content = f.readlines()

    # Extract number of objects and number of features
    while content[0][0] == '@':
        content.pop(0)
    n = len(content)
    d = len(content[0].split(','))

    # Extract feature values
    ls = []
    for i in range(n):
        if content[i] == '\n':
            continue
        ls.append([])
        for j in range(d):
            entry = content[i].split(',')[j]
            if '\n' in entry:
                entry = entry.replace('\n', '')
            ls[i].append(entry)
    # Create DataFrame
    df = pd.DataFrame(ls)

    return df


def preprocess_and_export(df, dataset, folder):

    # Convert all columns except last one to float
    for col in df.columns[:-1]:
        df[col] = df[col].astype('float64')

    # Adjust column names
    df.columns = ['x' + str(i) for i in range(len(df.columns) - 1)] + ['class']

    # Encode class column as categorical
    categories = df['class'].unique()
    df['class'] = pd.Categorical(df['class'], categories).codes

    # Standardize features
    scaler = StandardScaler()
    df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

    # Export processed data set
    df.to_csv('data/processed data/' + folder + '/' + dataset + '_data.csv', index=False)


def process_dataset(dataset, folder):
    # Read raw data
    df = get_data_from_dat_file(dataset, folder)

    # Perform preprocessing
    preprocess_and_export(df, dataset, folder)


def generate_hard_constraints(folder, dataset, param_nf, random_state):
    # Import data set
    df = pd.read_csv('data/processed data/' + folder + '/' + dataset + '_data.csv')

    # Extract class labels
    y = df['class']

    # Get number of objects
    n = df.shape[0]

    # Determine number of constraints
    n_f = np.ceil(n * param_nf)
    n_constraints = int((n_f * (n_f - 1) / 2))

    if n_constraints == 0:
        constraints = {'ml': [], 'cl': [], 'sml': [], 'scl': [], 'sml_proba': [], 'scl_proba': []}
        file_name = ('data/processed data/' + folder + '/constraint sets/' + dataset
                     + '_constraints_' + '{:g}'.format(param_nf) + '.json')
        with open(file_name, 'w') as fp:
            json.dump(constraints, fp)
    else:
        # Set random state
        np.random.seed(random_state)

        counter = 0
        while counter < n_constraints:
            i = np.random.randint(0, n, size=n_constraints)
            j = np.random.randint(0, n, size=n_constraints)
            new_matrix = np.tile((i, j), reps=1).T

            # Sort indices
            min_row = new_matrix.min(axis=1)
            max_row = new_matrix.max(axis=1)

            # Remove entries on diagonal of affinity matrix
            idx = min_row != max_row
            min_row = min_row[idx]
            max_row = max_row[idx]
            new_matrix = np.tile((min_row, max_row), reps=1).T

            if counter == 0:
                current_matrix = np.unique(new_matrix, axis=0)
            else:
                current_matrix = np.unique(np.concatenate((current_matrix, new_matrix)), axis=0)

            counter = current_matrix.shape[0]

        i = current_matrix[:n_constraints, 0]
        j = current_matrix[:n_constraints, 1]

        # Extract ml and cl pairs based on ground truth
        idx_ml = y[i].values == y[j].values
        idx_cl = ~idx_ml
        ml = list(zip(i[idx_ml].tolist(), j[idx_ml].tolist()))
        cl = list(zip(i[idx_cl].tolist(), j[idx_cl].tolist()))

        # Export ml and cl constraints into json file
        constraints = {'ml': ml, 'cl': cl, 'sml': [], 'scl': [], 'sml_proba': [], 'scl_proba': []}
        file_name = ('data/processed data/' + folder + '/constraint sets/' + dataset
                     + '_constraints_' + '{:g}'.format(param_nf) + '.json')
        with open(file_name, 'w') as fp:
            json.dump(constraints, fp)


def generate_noisy_constraints(folder, dataset, param_nf, random_state, lower_bound):
    df = pd.read_csv('data/processed data/' + folder + '/' + dataset + '_data.csv')
    y = df['class']
    n = df.shape[0]
    n_f = np.ceil(n * param_nf)
    n_constraints = int((n_f * (n_f - 1) / 2))

    # Set random state
    np.random.seed(random_state)

    counter = 0
    while counter < n_constraints:
        i = np.random.randint(0, n, size=n_constraints)
        j = np.random.randint(0, n, size=n_constraints)
        new_matrix = np.tile((i, j), reps=1).T

        # Sort indices
        min_row = new_matrix.min(axis=1)
        max_row = new_matrix.max(axis=1)
        new_matrix = np.tile((min_row, max_row), reps=1).T

        if counter == 0:
            current_matrix = np.unique(new_matrix, axis=0)
        else:
            current_matrix = np.unique(np.concatenate((current_matrix, new_matrix)), axis=0)

        counter = current_matrix.shape[0]

    i = current_matrix[:n_constraints, 0]
    j = current_matrix[:n_constraints, 1]

    probability_values = lower_bound + (1 - lower_bound) * np.random.rand(n_constraints)

    correct_constraint_type = (y[i].values == y[j].values) * 1
    incorrect_constraint_type = 1 - correct_constraint_type
    random_values = np.random.rand(n_constraints)
    ind_correct = probability_values >= random_values
    ind_incorrect = ~ind_correct
    constraint_type = correct_constraint_type.copy()
    constraint_type[ind_incorrect] = incorrect_constraint_type[ind_incorrect].copy()

    # Extract ml and cl pairs based on ground truth
    idx_sml = constraint_type == 1
    idx_scl = constraint_type == 0
    sml = list(zip(i[idx_sml].tolist(), j[idx_sml].tolist()))
    scl = list(zip(i[idx_scl].tolist(), j[idx_scl].tolist()))
    sml_weights = 2 * (probability_values[idx_sml] - 0.5)
    scl_weights = 2 * (probability_values[idx_scl] - 0.5)

    # Export ml and cl constraints into json file
    constraints = {'ml': [], 'cl': [], 'sml': sml, 'scl': scl, 'sml_proba': sml_weights.tolist(),
                   'scl_proba': scl_weights.tolist()}
    file_name = ('data/processed data/' + folder + '/noisy constraint sets/' + dataset + '_noisy_constraints_'
                 + '{:.2f}'.format(lower_bound) + '_' + '{:g}'.format(param_nf) + '.json')
    with open(file_name, 'w') as fp:
        json.dump(constraints, fp)
