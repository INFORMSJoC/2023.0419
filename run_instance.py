# © 2024, University of Bern, Group for Business Analytics, Operations Research and Quantitative Methods,
# Philipp Baumann

# %% Import packages
import json
import pandas as pd
import numpy as np
from src.pccc import pccc
from sklearn.metrics import adjusted_rand_score

# %% Select data and constraint set

dataset = 'data/processed data/COL1/appendicitis_data.csv'
constraint_set = 'data/processed data/COL1/constraint sets/appendicitis_constraints_0.15.json'

# %% Load dataset

df = pd.read_csv(dataset)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
n_clusters = len(np.unique(y))

# %% Load constraints
constraints = json.load(open(constraint_set))
ml = constraints['ml']
sml = constraints['sml']
cl = constraints['cl']
scl = constraints['scl']
sml_weights = constraints['sml_proba']
scl_weights = constraints['scl_proba']

if not sml_weights:
    sml_weights = None
if not scl_weights:
    scl_weights = None

# %% Apply PCCC algorithm
output = pccc(X, n_clusters,
              ml=ml,
              cl=cl,
              sml=sml,
              scl=scl,
              sml_weights=sml_weights,
              scl_weights=scl_weights,
              cluster_repositioning='violations_inertia',  # ='none'
              dynamic_n_neighbors='n_violations_neighbors.500.10.after_repositioning',  # ='none'
              random_state=24)

# %% Evaluate assignment
print('ARI: ', adjusted_rand_score(y, output['labels']))
