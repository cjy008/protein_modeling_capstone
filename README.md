Protein Modeling Capstone
=========================== 

[TOC]

# Getting Started
## Creating the conda environment
There are two environment files currently available for ESM and Tape. 
```
# For the ESM environment:
conda env create -f environment/esm_environment.yml --name esm

# For the Tape environment:
conda env create -f environment/tape_environment.yml --name tape
``` 

## Activate the conda environment
```
# Activate the ESM environment
conda activate esm

# Activate the Tape environment
conda activate tape
```

### Deactivating the environment
```
conda deactivate
```