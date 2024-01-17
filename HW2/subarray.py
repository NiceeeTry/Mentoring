MINUS_INFINITY = float("-inf")


def max_subarray_sum(nums):
    if not nums:
        return

    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


def max_subarray_sum_2(nums):
    pass


def max_subarray_sum_length_range(nums, A, B):
    if not nums or A > B or A <= 0 or B <= 0:
        return

    max_sum = MINUS_INFINITY
    curr_sum = 0
    curr_length = 0
    left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        curr_length += 1

        while curr_length > B or curr_sum < nums[right]:
            curr_sum -= nums[left]
            left += 1
            curr_length -= 1

        if A <= curr_length <= B:
            max_sum = max(max_sum, curr_sum)

    return max_sum if max_sum != MINUS_INFINITY else None



def max_subarray_sum_quadratic(arr, A, B):

    n = len(arr)
    max_sum = MINUS_INFINITY

    for i in range(n):
        for j in range(i, min(i + B, n)):
            current_sum = sum(arr[i:j+1])

            if A <= j - i + 1 <= B:
                max_sum = max(max_sum, current_sum)

    return max_sum


a = [-34, 97, 26, -15, -93, -11, -89, -97, 93, 94]
A, B = 1, 3
# # 108
# # 187            
# res1 = max_subarray_sum_quadratic(a, A,B)
# res2 = func(a, A,B)
# print(res1, res2)

def max_subarray_sum_with_k_elem(nums, k):
    left = 0
    counter = {}
    curr_sum = 0
    max_sum = MINUS_INFINITY

    for right in range(len(nums)):
        num = nums[right]

        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

        curr_sum += num

        while counter[num] > 1 or (right - left + 1) > k:
            curr_sum -= nums[left]
            counter[nums[left]] -= 1
            left += 1

        if right - left + 1 == k:
            max_sum = max(max_sum, curr_sum)

    return max_sum if max_sum != MINUS_INFINITY else None


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [5, 4, -1, 7, 8]
arr = [1, -2, 3, 10, -4, 7, 2, -5]
arr3 = [1, 5, 4, 2, 9, 9, 9]
arr4 = [4, 4, 4]

# print(max_subarray_sum(arr2))
# print(max_subarray_sum_length_range(arr, 1,4))
# print(max_subarray_sum_quadratic(arr, 1, 4))
# print(max_subarray_sum_with_k_elem(arr1, 4))
# print(max_subarray_sum_with_k_elem(arr4, 3))

import random

def test_range():
    size = 10
    arr = [random.randint(-100, 100) for _ in range(size)]

    # print(matrix)
    for A in range(1, size):
        for B in range(A + 1, size):
            try :
                assert max_subarray_sum_quadratic(arr, A, B) == func(arr, A, B)
            except:
                print(arr, A, B)
                print(func(arr, A, B))
                print(max_subarray_sum_quadratic(arr, A, B))

            # print(max_subarray_sum_length_range(arr, A, B))

# test_range()

