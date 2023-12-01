from typing import List


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3, 1]
# Output: true
# Example
# 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: false
# Example
# 3:
#
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true


def contains_duplicate_brute(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Args:
         nums (List[int]): List of integers representing the array

    Returns:
        bool: Boolean representing if the input array contains a duplicate or not
    """
    try:
        if not all(isinstance(x, int) for x in nums):
            raise TypeError("Input must be a list of integers.")
        if not nums:
            raise ValueError("Input array cannot be empty.")

        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    return True

        return False

    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")


def contains_duplicate_linear(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Args:
         nums (List[int]): List of integers representing the array

    Returns:
        bool: Boolean representing if the input array contains a duplicate or not
    """
    try:
        if not all(isinstance(x, int) for x in nums):
            raise TypeError("Input must be a list of integers.")
        if not nums:
            raise ValueError("Input array cannot be empty.")

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")


print(contains_duplicate_linear([1, 2, 3, 1]))
print(contains_duplicate_linear([1, 2, 3, 4]))
print(contains_duplicate_linear([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
