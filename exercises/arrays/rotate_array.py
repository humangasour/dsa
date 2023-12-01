# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
from typing import List


def rotate_once(nums: List[int]):
    """
    Rotates the input array to the right once

    Args:
        nums (List[int]): List of integers representing the array

    Returns:
        None: Modifies the input array in place
    """
    last_element = nums.pop()
    nums.insert(0, last_element)


def rotate_array_brute(nums: List[int], k: int):
    """
    Rotates the input array to the right by k steps

    Args:
        nums (List[int]): List of integers representing the array
        k (int): Number of steps to rotate the array

    Returns:
        None: Modifies the input array in place
    """
    k = k % len(nums)
    for _ in range(k):
        rotate_once(nums)

# time complexity - O(k*n)
# space complexity - O(1)
