from src.utils import dtw

def cluster_divide_and_conquer(segments, min_size=15, depth=0):
    # Returns a list of clusters (each cluster: list of segments)
    if len(segments) <= min_size:
        return [segments]
    # Find furthest pair to act as pivots
    furthest = (0, 0)
    max_dist = -1
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            dist = dtw(segments[i], segments[j])
            if dist > max_dist:
                max_dist = dist
                furthest = (i, j)
    pivot1, pivot2 = segments[furthest[0]], segments[furthest[1]]
    cluster1 = []
    cluster2 = []
    for seg in segments:
        d1 = dtw(seg, pivot1)
        d2 = dtw(seg, pivot2)
        if d1 < d2:
            cluster1.append(seg)
        else:
            cluster2.append(seg)
    # Recurse
    return cluster_divide_and_conquer(cluster1, min_size, depth+1) + \
           cluster_divide_and_conquer(cluster2, min_size, depth+1)
