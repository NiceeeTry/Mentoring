def sum_of_subarray(arr, S):
    sum_dict = {}
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num
        sum_dict[current_sum] = i

        if current_sum - S in sum_dict:
            start = sum_dict[current_sum - S] + 1
            end = i
            return start, end
    return -1, -1

arr = [1, 4, 20, 3, 10, 5]
S = 13

print(sum_of_subarray(arr, S))


