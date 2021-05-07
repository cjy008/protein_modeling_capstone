#!/usr/bin/env bash

#SBATCH --job-name=tape-0.4-fake_enzyme_test
#SBATCH --account=use300
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=93G
#SBATCH --gpus=1
#SBATCH --time=00:30:00
#SBATCH --output=%x.o%j.%N

declare -xr SINGULARITY_MODULE='singularitypro/3.5'
declare -xr SINGULAIRTY_CONTAINER_DIR='/cm/shared/apps/containers/singularity'

module purge
module load "${SINGULARITY_MODULE}"
module list
printenv

time -p singularity exec --bind /expanse,/scratch --nv "${SINGULAIRTY_CONTAINER_DIR}/ciml/tape-0.4-20210427.sif" python -u run_tape.py