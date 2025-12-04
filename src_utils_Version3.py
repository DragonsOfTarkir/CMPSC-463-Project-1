import numpy as np
import pandas as pd

# ---------------------------
# DATA LOADING
# ---------------------------
def load_abp_segments(filename):
    """
    Load PulseDB ABP segments from CSV file.
    Each row should correspond to a single segment.
    Returns: list of 1D numpy arrays.
    """
    segments = []
    df = pd.read_csv(filename)
    for idx, row in df.iterrows():
        segments.append(row.values.astype(float))
    return segments

# ---------------------------
# DTW DISTANCE FUNCTION
# ---------------------------
def dtw(ts1, ts2):
    """
    Classic DTW calculation for two time-series.
    Arguments:
        ts1: first time-series (1D array)
        ts2: second time-series (1D array)
    Returns:
        distance (float)
    """
    n = len(ts1)
    m = len(ts2)
    dtw_matrix = np.full((n + 1, m + 1), np.inf)
    dtw_matrix[0, 0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(ts1[i-1] - ts2[j-1])
            min_prev = min(
                dtw_matrix[i-1, j],    # insertion
                dtw_matrix[i, j-1],    # deletion
                dtw_matrix[i-1, j-1]   # match
            )
            dtw_matrix[i, j] = cost + min_prev
    return dtw_matrix[n, m]