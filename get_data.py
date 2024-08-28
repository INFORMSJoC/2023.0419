# © 2024, University of Bern, Group for Business Analytics, Operations Research and Quantitative Methods,
# Philipp Baumann

import os
from data.download_raw_data import download_raw_data_of_collection_1, download_raw_data_of_collection_4
from data.prepare_data_sets_of_collection_1 import prepare_collection_1
from data.prepare_data_sets_of_collection_2 import prepare_collection_2
from data.prepare_data_sets_of_collection_3 import prepare_collection_3
from data.prepare_data_sets_of_collection_4 import prepare_collection_4
from data.prepare_constraint_sets_for_collection_1 import prepare_constraint_sets_for_collection_1, \
    generate_noisy_constraint_sets_for_collection_1, generate_additional_constraint_sets_for_collection_1
from data.generate_constraint_sets_for_collection_2 import generate_constraint_sets_for_collection_2
from data.generate_constraint_sets_for_collection_3 import generate_constraint_sets_for_collection_3
from data.generate_constraint_sets_for_collection_4 import generate_constraint_sets_for_collection_4

# %% Create folders and download raw data
data_not_yet_downloaded = True
if data_not_yet_downloaded:
    os.makedirs('data/raw data/COL4')
    os.makedirs('data/processed data/COL1/constraint sets')
    os.makedirs('data/processed data/COL1/noisy constraint sets')
    os.makedirs('data/processed data/COL2/constraint sets')
    os.makedirs('data/processed data/COL3/constraint sets')
    os.makedirs('data/processed data/COL4/constraint sets')

    download_raw_data_of_collection_1()
    download_raw_data_of_collection_4()

# %% Prepare data sets
prepare_collection_1()
prepare_collection_2()
prepare_collection_3()
prepare_collection_4()

# %% Prepare constraint sets
prepare_constraint_sets_for_collection_1()
generate_additional_constraint_sets_for_collection_1()

# %% Generate constraint sets
generate_constraint_sets_for_collection_2()
generate_constraint_sets_for_collection_3()
generate_constraint_sets_for_collection_4()

# %% Generate noisy constraint sets
generate_noisy_constraint_sets_for_collection_1(['appendicitis', 'moons', 'zoo'])
