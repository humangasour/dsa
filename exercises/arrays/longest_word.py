import re


def longest_word(sentence: str):
    """
    Find the longest word in a given string.

    Args:
        sentence (string): A string from which to find the longest word

    Returns:
        str: The longest word in the string
    """
    # Remove punctuation using regex
    cleaned_string = re.sub(r'[^\w\s]', '', sentence)

    # Split the string into words
    words = cleaned_string.split()

    # Find the longest word
    longest = max(words, key=len)

    return longest
