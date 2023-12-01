from typing import List


def move_zeroes_brute(nums: List[int]):
    """
    Given an array of integers, move all 0's to the end of it while maintaining the relative order of non-zero elements

    Args:
        nums(List[int]): List of integers representing the array

    Returns:
        None: The function modifies the input list in place
    """
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] == 0:
            for j in range(i, n-1):
                nums[j], nums[j+1] = nums[j+1], nums[j]
            n -= 1
        else:
            i += 1

# time complexity - O(n^2)
# space complexity - O(1)


def move_zeroes_linear(nums: List[int]):
    """
    Given an array of integers, move all 0's to the end of it while maintaining the relative order of non-zero elements

    Args:
        nums(List[int]): List of integers representing the array

    Returns:
        None: The function modifies the input list in place
    """
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


test_nums = [0, 1, 0, 3, 12]
move_zeroes_linear(test_nums)
print(test_nums)
