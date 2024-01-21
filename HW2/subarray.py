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


def max_subarray_sum_length_range(nums, A, B):
    if not nums or A > B or A <= 0 or B <= 0:
        return
    max_sum = MINUS_INFINITY
    curr_sum = 0
    curr_length = 0
    left = 0

    for right in range(len(nums)):
        if A <= curr_length <= B:
            max_sum = max(max_sum, curr_sum)

        curr_sum += nums[right]
        curr_length += 1

        if A <= curr_length <= B:
            max_sum = max(max_sum, curr_sum)

        while curr_length > B or curr_sum < nums[right]:
            curr_sum -= nums[left]
            left += 1
            curr_length -= 1
        
        if A <= curr_length <= B:
            max_sum = max(max_sum, curr_sum)

    return max_sum



def max_subarray_sum_quadratic(arr, A, B):

    n = len(arr)
    max_sum = MINUS_INFINITY

    for i in range(n):
        for j in range(i, min(i + B, n)):
            current_sum = sum(arr[i:j+1])

            if A <= j - i + 1 <= B:
                max_sum = max(max_sum, current_sum)

    return max_sum


def func(arr, a, b):
    prefix_sums = [0]
    for num in arr:
        prefix_sums.append(prefix_sums[-1] + num)
    # print(prefix_sums)
    n = len(arr)
    d = b - a
    deq = []
    answer = float('-inf')

    for i in range(a, n + d + 1):
        # print(deq, "deq")
        if deq and deq[0][1] < i - d:
            deq.pop(0)

        if i <= n:
            # Pop from back of deque (now a list)
            while deq and deq[-1][0] <= prefix_sums[i]:
                deq.pop()

            deq.append((prefix_sums[i], i))

        if i >= b:
            # deq[0][0] is the maximum element of prefix_sums in the range [i-d, min(n, i)]
            answer = max(answer, deq[0][0] - prefix_sums[i - b])

    return answer

a = [80, -25, 69, 36, 94, -44, -39, 97, -95, 30]
# 174
# 199


A, B = 1, 4
    
res1 = max_subarray_sum_quadratic(a, A, B)
# res2 = max_subarray_sum_length_range(a, A, B)
# func(a, A, B)
res2 = func(a, A, B)
print(res1, res2)

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

test_range()

