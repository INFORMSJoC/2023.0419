import shutil
import requests
import zipfile
import tarfile
import gzip
import os

# Store urls of data sets (valid as of April 2022)
links_to_data_sets = {
    'appendicitis': "https://sci2s.ugr.es/keel/dataset/data/classification/appendicitis.zip",
    'banana': "https://sci2s.ugr.es/keel/dataset/data/classification/banana.zip",
    'breast_cancer':
        "https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-wisconsin-diagnostic-dataset",
    'bupa': "https://sci2s.ugr.es/keel/dataset/data/classification/bupa.zip",
    'cifar-10': "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz",
    'cifar-100': "https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz",
    'circles': "https://raw.githubusercontent.com/GermangUgr/DILS_CC/master/ToyDatasets/circles_toydataset.txt",
    'ecoli': "https://sci2s.ugr.es/keel/dataset/data/classification/ecoli.zip",
    'glass': "https://sci2s.ugr.es/keel/dataset/data/classification/glass.zip",
    'haberman': "https://sci2s.ugr.es/keel/dataset/data/classification/haberman.zip",
    'hayesroth': "https://sci2s.ugr.es/keel/dataset/data/classification/hayes-roth.zip",
    'heart': "https://sci2s.ugr.es/keel/dataset/data/classification/heart.zip",
    'ionosphere': "https://sci2s.ugr.es/keel/dataset/data/classification/ionosphere.zip",
    'iris': "https://sci2s.ugr.es/keel/dataset/data/classification/iris.zip",
    'led7digit': "https://sci2s.ugr.es/keel/dataset/data/classification/led7digit.zip",
    'letter': "https://sci2s.ugr.es/keel/dataset/data/classification/letter.zip",
    'mnist': ["https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz",
              "https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz",
              "https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz",
              "https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz"],
    'monk2': "https://sci2s.ugr.es/keel/dataset/data/classification/monk-2.zip",
    'moons': "https://raw.githubusercontent.com/GermangUgr/DILS_CC/master/ToyDatasets/moons_toydataset.txt",
    'movement_libras': "https://sci2s.ugr.es/keel/dataset/data/classification/movement_libras.zip",
    'newthyroid': "https://sci2s.ugr.es/keel/dataset/data/classification/newthyroid.zip",
    'saheart': "https://sci2s.ugr.es/keel/dataset/data/classification/saheart.zip",
    'shuttle': "https://sci2s.ugr.es/keel/dataset/data/classification/shuttle.zip",
    'sonar': "https://sci2s.ugr.es/keel/dataset/data/classification/sonar.zip",
    'soybean': "https://archive.ics.uci.edu/ml/machine-learning-databases/soybean/soybean-small.data",
    'spectfheart': "https://sci2s.ugr.es/keel/dataset/data/classification/spectfheart.zip",
    'spiral': "https://raw.githubusercontent.com/GermangUgr/DILS_CC/master/ToyDatasets/spiral_toydataset.txt",
    'tae': "https://sci2s.ugr.es/keel/dataset/data/classification/tae.zip",
    'vehicle': "https://sci2s.ugr.es/keel/dataset/data/classification/vehicle.zip",
    'wine': "https://sci2s.ugr.es/keel/dataset/data/classification/wine.zip",
    'zoo': "https://sci2s.ugr.es/keel/dataset/data/classification/zoo.zip"}


def download_raw_data_of_collection_1():
    path = 'data/raw data/COL1/'

    zip_files = ['appendicitis', 'bupa', 'ecoli', 'glass', 'haberman', 'hayesroth', 'heart', 'ionosphere', 'iris',
                 'led7digit', 'monk2', 'movement_libras', 'newthyroid', 'saheart', 'sonar', 'spectfheart', 'tae',
                 'vehicle', 'wine', 'zoo']

    for name in zip_files:
        # Download file
        response = requests.get(links_to_data_sets[name])
        file_name = path + name + '_data.zip'
        open(file_name, 'wb').write(response.content)

        # Extract zip file
        zipfile.ZipFile(file_name, 'r').extractall(path)

        # Delete zip file
        os.remove(file_name)

        # Print progress
        print('Data set', name, 'successfully downloaded.')

    text_files = ['circles', 'moons', 'spiral']

    for name in text_files:
        # Download file
        response = requests.get(links_to_data_sets[name])
        file_name = path + name + '_toydataset.txt'
        open(file_name, 'wb').write(response.content)

        # Print progress
        print('Data set', name, 'successfully downloaded.')

    data_files = ['soybean']

    for name in data_files:
        # Download file
        response = requests.get(links_to_data_sets[name])
        file_name = path + name + '-small.data'
        open(file_name, 'wb').write(response.content)

        # Print progress
        print('Data set', name, 'successfully downloaded.')


def download_raw_data_of_collection_4():
    path = 'data/raw data/COL4/'

    zip_files = ['banana', 'letter', 'shuttle']

    for name in zip_files:
        # Download file
        response = requests.get(links_to_data_sets[name])
        file_name = path + name + '_data.zip'
        open(file_name, 'wb').write(response.content)

        # Extract zip file
        zipfile.ZipFile(file_name, 'r').extractall(path)

        # Delete zip file
        os.remove(file_name)

        # Print progress
        print('Data set', name, 'successfully downloaded.')

    cifar_files = ['cifar-10', 'cifar-100']

    for name in cifar_files:
        # Download file
        response = requests.get(links_to_data_sets[name])
        file_name = path + name + '-python.tar.gz'
        open(file_name, 'wb').write(response.content)

        # Open file
        file = tarfile.open(file_name)

        # Extract file
        file.extractall(path)

        file.close()

        # Delete tar file
        os.remove(file_name)

        # Print progress
        print('Data set', name, 'successfully downloaded.')

    # Download mnist data
    links = links_to_data_sets['mnist']
    for link in links:
        response = requests.get(link)
        file_name = path + link.split('/')[-1]
        open(file_name, 'wb').write(response.content)

        # Extract file
        with gzip.open(file_name, 'rb') as f_in:
            with open(file_name.split('.')[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        # Delete gz file
        os.remove(file_name)

    # Print progress
    print('Data set mnist successfully downloaded.')
