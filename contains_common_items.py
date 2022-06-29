array1 = ['a', 'b', 'c', 'd', 1]
array2 = ['i', 'y', 'z', 1]


def contains_common_item(arr1: list, arr2: list):
    for i, _ in enumerate(arr1):
        for j, _ in enumerate(arr2):
            if arr1[i] == arr2[j]:
                return True
    return False


# time complexity - O(a * b)
# space complexity - O(1)

def contains_common_item_2(arr1: list, arr2: list) -> bool:
    obj = {}
    for character in arr1:
        if character not in obj:
            obj[character] = True

    for character in arr2:
        if character in obj:
            return True
    return False


# time complexity - O(a + b)
# space complexity - O(a)


print(contains_common_item_2(array1, array2))
