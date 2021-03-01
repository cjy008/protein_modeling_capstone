Protein Modeling Capstone
=========================== 

Table of Contents
===========================
* [Getting Started](#getting-started)
	* [Creating the conda environment](#creating-the-conda-environment)
	* [Activate the conda environment](#activate-the-conda-environment)
	* [Deactivating the environment](#deactivating-the-environment)

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