#!/bin/bash
#SBATCH --job-name=resource_test
#SBATCH --output=resource_output.txt
#SBATCH --cpus-per-task=120
#SBATCH --mem=100G
#SBATCH --time=01:00:00
#SBATCH --partition=research-bigmem

echo "CPUs allocated: $SLURM_CPUS_PER_TASK"

# Set Spark driver/executor memory
export PYSPARK_SUBMIT_ARGS="--driver-memory 60G --executor-memory 60G --conf spark.executor.cores=72 --conf spark.executor.instances=1 pyspark-shell"

singularity exec pyspark.sif python testing.py