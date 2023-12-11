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


def rotate_array_faster(nums: List[int], k: int):
    """
    Rotates the input array to the right by k steps

    Args:
        nums (List[int]): List of integers representing the array
        k (int): Number of steps to rotate the array

    Returns:
        None: Modifies the input array in place
    """
    n = len(nums)
    k = k % n
    rotated_array = [nums.pop() for _ in range(k)]
    rotated_array.reverse()
    rotated_array.extend(nums)
    nums[:] = rotated_array

# time complexity - O(n)
# space complexity - O(n)


def rotate_array_faster_with_less_space(nums: List[int], k: int):
    """
    Rotates the input array to the right by k steps

    Args:
        nums (List[int]): List of integers representing the array
        k (int): Number of steps to rotate the array

    Returns:
        None: Modifies the input array in place
    """
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    print(nums)

# time complexity - O(n)
# space complexity - O(1)


rotate_array_faster_with_less_space([1, 2, 3, 4, 5, 6, 7], 3)
