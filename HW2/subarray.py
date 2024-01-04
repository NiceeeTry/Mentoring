def max_subarray_sum(nums):
    if not nums:
        return None

    max_sum= nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

def max_subarray_sum_2(nums):
    pass

def max_subarray_sum_length_range(nums, A, B):
    if not nums or A > B or A <= 0 or B <= 0:
        return None

    max_sum = float('-inf')
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

    return max_sum if max_sum != float('-inf') else None


def max_subarray_sum_with_k_elem(nums, k):
    if not nums or k > len(nums):
        return None

    l, r = 0, k
    max_sum = 0
    unique = set()
    i = 0
    while len(unique) < k and i < len(nums):
        max_sum += nums[i]
        unique.add(nums[i])
        i += 1

    curr_sum = max_sum
    while r < len(nums):
        print(r, unique, curr_sum, max_sum)
        while r < len(nums) and nums[r] in unique:
            curr_sum += nums[r]
            r+=1
        if r < len(nums):
            curr_sum = curr_sum - nums[l] + nums[r]
            unique.add(nums[r])
            unique.discard(nums[l])
            max_sum = max(max_sum, curr_sum)
            r+=1
            l+=1
    return max_sum




arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [5,4,-1,7,8]
arr = [1, -2, 3, 10, -4, 7, 2, -5]
arr3 = [1,5,4,2,9,9,9]
arr4 = [4,4,4]

# print(max_subarray_sum(arr2))
# print(max_subarray_sum_with_k_elem(arr1, 4))
# max_subarray_sum_with_length(arr1, 1, 1)
# print(max_subarray_sum_length_range(arr1, 1,1))
print(max_subarray_sum_with_k_elem(arr4, 3))


