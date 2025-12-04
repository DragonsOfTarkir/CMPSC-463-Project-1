def kadane(ts):
    """
    Classic Kadane's algorithm for max subarray.
    Returns: start index, end index, max sum
    """
    max_sum = None
    cur_sum = 0
    start = 0
    end = 0
    tmp_start = 0
    for i, val in enumerate(ts):
        if cur_sum <= 0:
            cur_sum = val
            tmp_start = i
        else:
            cur_sum += val
        if max_sum is None or cur_sum > max_sum:
            max_sum = cur_sum
            start = tmp_start
            end = i
    return start, end, max_sum
