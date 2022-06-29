array1 = [1, 3, 4, 6]  # 8
array2 = [1, 2, 5, 7]  # 12


# PROBLEM:
# given an array and a total
# check if any two numbers in the array add up to be equal to the total
# return true if yes
# return false if not


def has_pair_with_sum(arr: list, total: int) -> bool:
    # if arrays are sorted
    # we can loop through every index and pair it with every other index to see if the some matches
    for i, num in enumerate(arr):
        for j, other_num in enumerate(arr[i + 1:]):
            if num + other_num == total:
                return True
    return False

# time complexity - O(n^2)
# space complexity - O(1)


def has_pair_with_sum_2(arr: list[int], total: int) -> bool:
    # arrays are still sorted
    # making this one more time efficient
    # since it sorted, we can check for the sum of first and last values
    # if it is equal to the sum, we return true
    # if it is lower than the sum, we move on to the next highest value
    # if it is higher than the sum, we move on to the next lowest value
    low = 0
    high = len(arr) - 1
    while low < high:
        add = arr[low] + arr[high]
        if add == total:
            return True
        elif add < total:
            low += 1
        else:
            high -= 1
    return False

# time complexity - O(n)
# space complexity - O(n)


unsorted_array_1 = [3, 1, 2, 6]  # 6
unsorted_array_2 = [6, 7, 1, 4, 8]  # 15


def has_pair_with_sum_3(arr: list[int], total: int) -> bool:
    # arrays are not sorted this time
    # loop through every value and save it's complement in a set
    # check if the set has a value equal to the current value in loop
    # return true if yes
    # return false if not
    compliments = set()
    for item in arr:
        if item in compliments:
            return True
        compliments.add(total - item)
    return False

# time complexity - O(n)
# space complexity - O(n)
