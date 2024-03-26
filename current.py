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

def contains_common_items_brute(array1, array2):
    """
    Determines if two arrays contain any common items using a brute-force approach.

    Args:
    array1 (List[Any]): The first array to compare.
    array2 (List[Any]): The second array to compare.

    Returns:
    bool: True if there is at least one common item, False otherwise.

    Raises:
    TypeError: If input arguments are not lists.

    Examples:
    >>> contains_common_items(['a', 'b', 'c', 'x'], ['x', 'y', 'z'])
    True
    >>> contains_common_items(['a', 'b', 'c'], ['x', 'y', 'z'])
    False
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
