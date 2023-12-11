from typing import List, Union


def first_recurring_char(chars: List[Union[str, int]]) -> Union[str, int, None]:
    """
    Returns the first recurring character from the list of characters, returns None if there is no such character

    Args:
        chars (List[Union[str, int]]): List of characters represented as strings or integers

    Returns:
        Union[str, int, None]: First recurring character or None if there is no such character
    """
    if not chars:
        raise ValueError("No characters")

    if not all(isinstance(char, (str, int)) for char in chars):
        raise TypeError("All characters must be either string or int")

    if len(chars) < 1:
        return None

    char_set = set()

    for char in chars:
        if char in char_set:
            return char
        char_set.add(char)

    return None


print(first_recurring_char([""]))
print(first_recurring_char(['a', 'b', 'a', 'c']))
print(first_recurring_char(['a', 'b', 'b', 'c']))
