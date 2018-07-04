#!/bin/bash

cd Desktop/CISRO_HPC/sparse_learning_weight/

module load matlab/R2016a


matlab -nojvm -nodisplay -r 'weight_KSVD.m'
