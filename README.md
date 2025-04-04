# HPC Spark Demo

This repository demonstrates running a Spark-based logistic regression job on the HIGGS dataset using MTSU’s Babbage HPC cluster.

---

## Contents

1. **`testing.py`**  
   - Python code for Spark parallelization.  
   - Requests **72 cores** and **60 GB** of RAM.

2. **`submit_job.sh`**  
   - Shell script to submit the Spark job to MTSU’s Babbage cluster.

3. **`container_def`**  
   - Singularity container definition file for building the `pyspark.sif` container.

---

## Requirements

1. **Singularity Container (`pyspark.sif`)**  
   - Download from [Google Drive](https://drive.google.com/file/d/1OjR70_HA3F5vHIizRkhZWX4s_s6mbejM/view?usp=drive_link),  
     **OR**  
   - Build locally from `container_def` using Singularity (e.g., `sudo singularity build pyspark.sif container_def`).

2. **HIGGS Dataset**  
   - Download from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/280/higgs).  
   - Place the CSV file (e.g., `HIGGS.csv`) in the appropriate location accessible by `testing.py`.

---

## Usage

1. **(Optional) Check Cluster Resources**  
   - Run `squeue` (or other cluster commands) to ensure necessary resources (cores/memory) are available.

2. **Submit the Job**  
   - Execute `./submit_job.sh`.  
   - The job submission script will request 72 cores, 60 GB RAM, and run the `testing.py` Spark job within the `pyspark.sif` container.

3. **Monitor**  
   - Use `squeue` again or similar commands (like `sacct`) to check the job status.
   - Logs will be saved according to your HPC cluster’s configuration or any settings within `submit_job.sh`.

---

## Notes

- **Spark Configuration**:  
  Inside `testing.py`, Spark is configured to utilize 72 cores and 60 GB of memory. Adjust these parameters as needed for your HPC environment.  
- **Data Path**:  
  Ensure the path to the HIGGS dataset in `testing.py` points to wherever you placed `HIGGS.csv`.  
- **Container vs. Host Dependencies**:  
  Using the `pyspark.sif` container helps encapsulate dependencies. If you need additional packages, modify the `container_def` or the container environment.

---

## Contact

- **Author**: Your Name (Thuan Nhan)  
- For questions or issues, please open an issue on this repository or contact me directly at `tnn2u@mtmail.mtsu.edu`.
