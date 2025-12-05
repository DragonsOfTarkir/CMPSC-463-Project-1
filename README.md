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
