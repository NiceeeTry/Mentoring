def subarray_with_max_sum(arr):
    if not arr:
        return None
    max_subarray = [0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(curr_sum + arr[i], arr[i])
        max_subarray = max(max_subarray, curr_sum)
    return max_subarray



def subarray_with_max_sum_2(arr):
    pass