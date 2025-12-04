import matplotlib.pyplot as plt
from src.utils import load_abp_segments
from src.clustering import cluster_divide_and_conquer
from src.closest_pair import get_closest_pair
from src.kadane import kadane

def demo_visualize_segment(ts, title=None):
    plt.plot(ts, color='blue')
    if title:
        plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("ABP Value")
    plt.show()

def main():
    filename = "data/pulsedb_abp_1000_segments.csv"
    segments = load_abp_segments(filename)
    print(f"Loaded {len(segments)} ABP segments.")
    clusters = cluster_divide_and_conquer(segments, min_size=18)
    print(f"Found {len(clusters)} clusters.")
    summary = []
    # For each cluster, find closest pair and max subarrays
    for ci, cluster in enumerate(clusters):
        pair_indices, pair_dist = get_closest_pair(cluster)
        ts1 = cluster[pair_indices[0]]
        ts2 = cluster[pair_indices[1]]
        interval1 = kadane(ts1)
        interval2 = kadane(ts2)
        print(f"> Cluster {ci}: size={len(cluster)}, closest_pair={pair_indices}, distance={pair_dist:.2f}")
        print(f"  Max interval ts1: {interval1}")
        print(f"  Max interval ts2: {interval2}")
        # Visualize the closest pair for demo
        demo_visualize_segment(ts1, f"Cluster {ci} - Closest Segment 1")
        demo_visualize_segment(ts2, f"Cluster {ci} - Closest Segment 2")
        summary.append({
            "cluster": ci,
            "size": len(cluster),
            "closest_pair": pair_indices,
            "distance": float(pair_dist),
            "max_interval_1": interval1,
            "max_interval_2": interval2
        })
    # Optionally: write summary to file etc.

if __name__ == '__main__':
    main()
