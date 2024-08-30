import pandas as pd
import numpy as np
import idx2numpy
import pickle
from data.utilities import preprocess_and_export, process_dataset


def process_dataset_cifar10():
    # Read raw data
    with open('data/raw data/COL4/cifar-10-batches-py/test_batch', 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    X = data[b'data']
    y = data[b'labels']
    for i in range(1, 6):
        with open('data/raw data/COL4/cifar-10-batches-py/data_batch_' + str(i), 'rb') as fo:
            data = pickle.load(fo, encoding='bytes')
        X = np.concatenate((X, data[b'data']))
        y = np.concatenate((y, data[b'labels']))

    # Create DataFrame
    df = pd.DataFrame(np.c_[X, y])

    # Perform preprocessing
    preprocess_and_export(df, 'cifar10', 'COL4')


def process_dataset_cifar100():
    # Read raw data
    with open('data/raw data/COL4/cifar-100-python/test', 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    X = data[b'data']
    y = data[b'fine_labels']
    with open('data/raw data/COL4/cifar-100-python/train', 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    X = np.concatenate((X, data[b'data']))
    y = np.concatenate((y, data[b'fine_labels']))

    # Create DataFrame
    df = pd.DataFrame(np.c_[X, y])

    # Perform preprocessing
    preprocess_and_export(df, 'cifar100', 'COL4')


def process_dataset_mnist():
    # Read raw data
    file = 'data/raw data/COL4/train-labels-idx1-ubyte'
    y = idx2numpy.convert_from_file(file)
    file = 'data/raw data/COL4/train-images-idx3-ubyte'
    X = idx2numpy.convert_from_file(file)
    X = X.reshape(60000, -1)
    file = 'data/raw data/COL4/t10k-labels-idx1-ubyte'
    y = np.concatenate((y, idx2numpy.convert_from_file(file)))
    file = 'data/raw data/COL4/t10k-images-idx3-ubyte'
    X = np.concatenate((X, idx2numpy.convert_from_file(file).reshape(10000, -1)))

    # Create DataFrame
    df = pd.DataFrame(np.c_[X, y])

    # Perform preprocessing
    preprocess_and_export(df, 'mnist', 'COL4')


# %% Process data sets of group g1
def prepare_collection_4():
    folder = 'COL4'
    process_dataset('banana', folder)
    process_dataset('letter', folder)
    process_dataset('shuttle', folder)
    process_dataset_cifar10()
    process_dataset_cifar100()
    process_dataset_mnist()

    print('Data sets from collection COL4 sucessfully processed.')
