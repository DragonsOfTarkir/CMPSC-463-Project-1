from src.utils import dtw

def get_closest_pair(cluster):
    # Returns indices and distance for closest pair in a cluster
    best = None
    best_dist = float("inf")
    for i in range(len(cluster)):
        for j in range(i+1, len(cluster)):
            dist = dtw(cluster[i], cluster[j])
            if dist < best_dist:
                best = (i, j)
                best_dist = dist
    return best, best_dist