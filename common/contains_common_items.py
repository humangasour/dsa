# Contains Common Items
# Problem: Given two arrays, create a function that lets the user know (true/false) whether these two arrays contain any common items
#
# Example:
# array1 = ['a', 'b', 'c', 'd']
# array2 = ['x', 'y', 'z']
# should return False
# ----------------
# array1 = ['a', 'b', 'c', 'd']
# array2 = ['x', 'y', 'c']
# should return True
from typing import List

arr1 = ['a', 'b', 'c', 'x']
arr2 = ['x', 'y', 'z']


def contains_common_items_brute(array1: List[str], array2: List[str]) -> bool:
    """
    Determines if two arrays contain any common items using a brute-force approach.

    Args:
    array1 (List[Any]): The first array to compare.
    array2 (List[Any]): The second array to compare.

    Returns:
    bool: True if there is at least one common item, False otherwise.

    Raises:
    TypeError: If input arguments are not lists.
    """
    # Basic input validation
    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Both arguments must be of type list.")

    # Iterate through each element in the first array
    for item1 in array1:
        # For each element, iterate through the second array and check for a match
        for item2 in array2:
            if item1 == item2:
                return True  # Return True immediately if a match is found

    return False
# time complexity - O(a * b)
# space complexity - O(1)


def contains_common_items_hashmap(array1: List[str], array2: List[str]) -> bool:
    """
    Determines if two arrays contain any common items using a hashmap for efficient lookup.

    Args:
    array1: The first array, elements of which will be stored in a hashmap.
    array2: The second array to be checked against the hashmap.

    Returns:
    True if there is at least one common item, False otherwise.

    Raises:
    TypeError: If input arguments are not lists.
    """
    # Basic input validation
    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Both arguments must be of type list.")

    item_map = {}  # Creating a hashmap to store elements of the first array
    for item in array1:
        item_map[item] = True

    for item in array2:  # Iterating through the second array
        if item in item_map:  # Constant-time lookup to check for common items
            return True

    return False
# time complexity - O(a + b)
# space complexity - O(a)


def contains_common_items_set(array1: List[str], array2: List[str]) -> bool:
    """
    Determines if two arrays contain any common items using a set for efficient lookup.

    Args:
    array1: The first array, elements of which will be stored in a set.
    array2: The second array to be checked against the set.

    Returns:
    True if there is at least one common item, False otherwise.

    Raises:
    TypeError: If input arguments are not lists.
    """
    # Basic input validation
    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Both arguments must be of type list.")

    # Create a set from the first array
    items_set = set(array1)

    # Iterate through the second array and check if any item exists in the set
    for item in array2:
        if item in items_set:  # Constant-time lookup to check for common items
            return True

    return False
# time complexity - O(a + b)
# space complexity - O(a)


def contains_common_items_two_sets(array1: List[str], array2: List[str]) -> bool:
    """
    Determines if two arrays contain any common items using two sets for efficient lookup.

    Args:
    array1: The first array, elements of which will be stored in a set.
    array2: The second array to be checked against the set.

    Returns:
    True if there is at least one common item, False otherwise.

    Raises:
    TypeError: If input arguments are not lists.
    """
    # Basic input validation
    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Both arguments must be of type list.")

    return bool(set(array1) & set(array2))
# time complexity - O(a + b)
# space complexity - O(a + b)


print(contains_common_items_brute(arr1, arr2))
print(contains_common_items_hashmap(arr1, arr2))
print(contains_common_items_set(arr1, arr2))
print(contains_common_items_two_sets(arr1, arr2))


