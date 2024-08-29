![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)

# The PCCC Algorithm

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper [An algorithm for clustering with confidence-based must-link and cannot-link constraints](https://doi.org/10.1287/ijoc.2023.0419) by P. Baumann and D.S. Hochbaum. The snapshot is based on 
[this SHA](https://github.com/phil85/PCCC-Algorithm/commit/78cd345dbc6c0d3680e724b2cbeb8a74c2dc99f2) 
in the development repository.

**Important: This code is being developed on an on-going basis at 
https://github.com/phil85/PCCC-Algorithm. Please go there if you would like to
get a more recent version or would like support.**

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2023.0419 

https://doi.org/10.1287/ijoc.2023.0419.cd

Below is the BibTex for citing this snapshot of the repository.

```
@misc{bauhoc2024pccc,
  author =        {P. Baumann and D.S. Hochbaum},
  publisher =     {INFORMS Journal on Computing},
  title =         {{An algorithm for clustering with confidence-based must-link and cannot-link constraints}},
  year =          {2024},
  doi =           {10.1287/ijoc.2023.0419.cd},
  url =           {https://github.com/INFORMSJoC/2023.0419},
  note =          {Available for download at https://github.com/INFORMSJoC/2023.0419},
}  
```

## Description

The PCCC algorithm is a clustering method that incorporates both hard and soft must-link and cannot-link constraints.

## Installation

1) Clone this repository
2) Install Gurobi (https://www.gurobi.com/). Gurobi is a commercial mathematical programming solver. Free academic licenses are available [here](https://www.gurobi.com/academia/academic-program-and-licenses/).
3) Crete a virtual environment

```
python -m venv venv
```

4) Activate the virtual environment and install the required Python packages using the following command: 

```
pip install -r requirements.txt
```

5) Run the following command to generate the data and constraint sets (this will take a few minutes):

```
python get_data.py
```

## Results

All detailed results are available in the [results](results) folder.

## Replicating

1) Run the following command to apply the PCCC algorithm to the illustrative example from the paper

```
python run_illustrative_example.py
```

2) Run the following command to apply the PCCC algorithm to a specific instance from the paper. You can change the data and constraint sets by modifying the file run_instance.py.  

```
python run_instance.py
```
Links to the code of the benchmark approaches are available in the paper.

## Ongoing Development

This code is being developed on an on-going basis at the author's
[Github site](https://github.com/phil85/PCCC-Algorithm).

## Support

For support in using this software please contact the corresponding author (philipp.baumann@unibe.ch). Note that the software has been tested on a Windows OS only. 
