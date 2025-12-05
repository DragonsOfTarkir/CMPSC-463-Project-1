# CMPSC-463-Project-1

# PulseDB Time-Series Clustering and Segment Analysis Project

This repository contains code for clustering and analyzing ABP segments from PulseDB using classical divide-and-conquer and search algorithms.

## Components

- **Clustering:** Top-down split using recursive similarity (DTW distance), no ML libraries used.
- **Closest Pair:** Within each cluster, find the most similar segment pair.
- **Maximum Subarray:** For each segment, mark the most "active" interval (Kadane's algorithm).
- **Visualization:** matplotlib plots for inspection.

## Usage

1. Place your CSV in `data/pulsedb_abp_1000_segments.csv` (each row = 1 segment).
2. Run:
    ```
    python main.py
    ```
3. Inspect console outputs and cluster visualizations.

## Structure

- `utils.py`: Data loading and simple DTW.
- `clustering.py`: Recursive clustering logic.
- `closest_pair.py`: Closest pair search.
- `kadane.py`: Kadane’s max subarray.
- `main.py`: Project pipeline and summary/report.

## Data: PulseDB

We use the [PulseDB](https://github.com/pulselabteam/PulseDB) dataset for 10-second ABP (Arterial Blood Pressure) segments.

**Instructions to prepare data:**
1. Download `Train_Subset.mat` from PulseDB shared cloud links (see their README section on Info Files).
2. Place the `.mat` file in the `data/` directory at the root of this repo (create the folder if it doesn’t exist).
3. Run the extraction script:
   ```bash
   pip install mat73 numpy
   python extract_abp.py
   ```
   This will create `data/abp_1000_segments.npy` (the extracted 1000 ABP segments).

*Note: Raw and extracted data files should not be committed to git; use `.gitignore` to prevent this.*
