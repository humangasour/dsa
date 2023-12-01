from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

    Returns:
        List[int]: The indices of the two numbers from `nums` that add up to `target`.
    """
    length = len(nums)

    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

# time complexity - O(n^2)
# space complexity - O(1)


def two_sum_faster(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

    Returns:
        List[int]: The indices of the two numbers from `nums` that add up to `target`.
    """
    value_to_index_map = {}

    for i, value in enumerate(nums):
        complement = target - value

        if complement in value_to_index_map:
            return [value_to_index_map[complement], i]

        value_to_index_map[value] = i

    return None

# time complexity - O(n)
# space complexity - O(n)
