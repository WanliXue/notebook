#!/bin/bash

#SBATCH --time=00:05:00
#SBATCH --mem=50MB
#SBATCH --ntasks-per-node=1

cd $HOME/Desktop/CISRO_HPC/sparse_learning_weight/

module load matlab/R2016a

matlab -nodisplay -nojvm -r "weight_KSVD.m"
