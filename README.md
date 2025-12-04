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
    python src/main.py
    ```
3. Inspect console outputs and cluster visualizations.

## Structure

- `src/utils.py`: Data loading and simple DTW.
- `src/clustering.py`: Recursive clustering logic.
- `src/closest_pair.py`: Closest pair search.
- `src/kadane.py`: Kadane’s max subarray.
- `src/main.py`: Project pipeline and summary/report.

No machine learning or AI used — all algorithms are standard.
