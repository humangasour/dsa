from typing import List

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


def max_subarray_sum_brute(nums: List[int]) -> int:
    """
    Find the maximum sum using the brute force approach

    Args:
        nums (List[int]): List of integers representing the array

    Returns:
        int: Integer representing the maximum subarray sum
    """
    largest_sum = float('-inf')
    length = len(nums)

    for i in range(length):
        current_sum = 0
        for j in range(i, length):
            current_sum += nums[j]
            if current_sum > largest_sum:
                largest_sum = current_sum

    return int(largest_sum)

# time complexity - O(n^2)
# space complexity - O(1)


def max_subarray_sum_linear(nums: List[int]) -> int:
    """
    Find the maximum subarray sum using Kadane's algorithm

    Args:
        nums (List[int]): List of integers representing the array

    Returns:
        int: Integer representing the maximum subarray sum
    """
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    return max_sum

# time complexity - O(n)
# space complexity - O(1)


def max_subarray_sum_dq(nums: List[int]) -> int:
    """
    Find the maximum subarray sum using Divide and Conquer approach

    Args:
        nums (List[int]): List of integers representing the array

    Returns:
        int: Integer representing the maximum subarray sum
    """
    def helper(low: int, high: int) -> int:
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        return max(
                helper(low, mid),
                helper(mid + 1, high),
                max_crossing_subarray(low, mid, high)
            )

    def max_crossing_subarray(low: int, mid: int, high: int) -> int:
        left_sum = float('-inf')
        total = 0
        for i in range(mid, low - 1, -1):
            total += nums[i]
            left_sum = max(left_sum, total)

        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, high + 1):
            total += nums[i]
            right_sum = max(right_sum, total)

        return left_sum + right_sum

    return helper(0, len(nums) - 1)

# time complexity - O(n log n)
# space complexity - O(log n)


print(max_subarray_sum_linear([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output should be 6
print(max_subarray_sum_linear([1]))  # Output should be 1
print(max_subarray_sum_linear([5, 4, -1, 7, 8]))  # Output should be 23

