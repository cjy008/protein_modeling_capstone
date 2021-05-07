#!/usr/bin/env bash

#SBATCH --job-name=esm-0.3.1-Enzymes_test_esm
#SBATCH --account=use300
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#SBATCH --mem=248G
#SBATCH --time=00:30:00
#SBATCH --output=%x.o%j.%N

declare -xr SINGULARITY_MODULE='singularitypro/3.5'
declare -xr SINGULAIRTY_CONTAINER_DIR='/cm/shared/apps/containers/singularity'

module purge
module load "${SINGULARITY_MODULE}"
module list
printenv

time -p singularity exec --bind /expanse,/scratch "${SINGULAIRTY_CONTAINER_DIR}/ciml/esm-0.3.1-20210427.sif" python -u run_esm.py