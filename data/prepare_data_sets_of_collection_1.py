import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from data.utilities import get_data_from_dat_file, preprocess_and_export, process_dataset


def process_dataset_breast_cancer():
    # Read raw data
    X, y = load_breast_cancer(return_X_y=True)

    # Create DataFrame
    df = pd.DataFrame(np.concatenate((X, y.reshape(-1, 1)), axis=1))

    # Perform preprocessing
    preprocess_and_export(df, 'breast_cancer', 'COL1')


def process_dataset_circles():
    # Read raw data
    df = pd.read_table('data/raw data/COL1/circles_toydataset.txt', sep=',', header=None)

    # Perform preprocessing
    preprocess_and_export(df, 'circles', 'COL1')


def process_dataset_moons():
    # Read raw data
    df = pd.read_table('data/raw data/COL1/moons_toydataset.txt', sep=',', header=None)

    # Perform preprocessing
    preprocess_and_export(df, 'moons', 'COL1')


def process_dataset_saheart():
    # Read raw data
    df = get_data_from_dat_file('saheart', 'COL1')

    # Add column names to encode one of the features as a binary feature
    df.columns = ['Sbp', 'Tobacco', 'Ldl', 'Adiposity', 'Famhist', 'Typea', 'Obesity', 'Alcohol', 'Age', 'class']
    df = df.replace({'Famhist': {'Present': '1', 'Absent': '0'}})

    # Perform preprocessing
    preprocess_and_export(df, 'saheart', 'COL1')


def process_dataset_soybean():
    # Read raw data
    df = pd.read_table('data/raw data/COL1/soybean-small.data', sep=',', header=None)

    # Perform preprocessing
    preprocess_and_export(df, 'soybean', 'COL1')


def process_dataset_spiral():
    # Read raw data
    df = pd.read_table('data/raw data/COL1/spiral_toydataset.txt', sep=',', header=None)

    # Perform preprocessing
    preprocess_and_export(df, 'spiral', 'COL1')


# %% Process data sets of collection COL1
def prepare_collection_1():
    folder = 'COL1'
    process_dataset('appendicitis', folder)
    process_dataset_breast_cancer()
    process_dataset('bupa', folder)
    process_dataset_circles()
    process_dataset('ecoli', folder)
    process_dataset('glass', folder)
    process_dataset('haberman', folder)
    process_dataset('hayes-roth', folder)
    process_dataset('heart', folder)
    process_dataset('ionosphere', folder)
    process_dataset('iris', folder)
    process_dataset('led7digit', folder)
    process_dataset('monk-2', folder)
    process_dataset_moons()
    process_dataset('movement_libras', folder)
    process_dataset('newthyroid', folder)
    process_dataset_saheart()
    process_dataset('sonar', folder)
    process_dataset_soybean()
    process_dataset('spectfheart', folder)
    process_dataset_spiral()
    process_dataset('tae', folder)
    process_dataset('vehicle', folder)
    process_dataset('wine', folder)
    process_dataset('zoo', folder)

    print('Data sets from collection COL1 sucessfully processed.')
