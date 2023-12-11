from typing import List, Union, Any

INITIAL_BUCKET_SIZE = 19


class HashTable:
    bucket_size: int
    hashmap: List

    def __init__(self):
        """
        Initialize a new HashTable instance and create the array for the hash table which has its length equal to a pre-decided prime number

        Returns:
            None
        """
        self.bucket_size = INITIAL_BUCKET_SIZE
        self.hashmap = [None] * self.bucket_size

    def _hash(self, key: str) -> int:
        """
        Returns the index for the key value to be stored at

        Args:
            key (str): A string representing the key to store

        Returns:
            int: Index of the hashmap to store the key value pair at
        """
        return len(key) % self.bucket_size

    def set(self, key: Union[str, int], value: Any):
        """
        Stores the key value pair in the hashmap

        Args:
            key (Union[str, int]): A string or an integer representing the key
            value (any): Value to be stored for the given key

        Raises:
            ValueError: If the key is None or an empty string
            TypeError: If the key is neither a string not an int
        """
        if not key:
            raise ValueError('key must not be None or empty.')

        if not isinstance(key, (str, int)):
            raise TypeError('key must be an instance of str or int.')

        index = self._hash(key)

        # Initialize the bucket if it's None
        if self.hashmap[index] is None:
            self.hashmap[index] = []

        # Check if key already exists in the hashmap, overwrite if yes
        for i, (existing_key, _) in enumerate(self.hashmap[index]):
            if existing_key == key:
                self.hashmap[index][i] = (key, value)
                return

        # If the key does not exist, append the new key-value pair
        self.hashmap.append((key, value))

    def get(self, key: Union[str, int]) -> Union[Any, None]:
        """
        Retrieves the value associated with the key from the hashmap.

        Args:
            key (Union[str, int]): The key to be retrieved.

        Returns:
            Union[Any, None]: The value associated with the key, or None if the key is not found.
        """
        if not key:
            raise ValueError('key must not be None or empty.')

        if not isinstance(key, (str, int)):
            raise TypeError('key must be an instance of str or int.')

        index = self._hash(key)

        if self.hashmap[index] is None:
            return None

        for existing_key, value in self.hashmap[index]:
            if existing_key == key:
                return value

        return None

    def remove(self, key: Union[str, int]) -> bool:
        """
        Removes the key-value pair associated with the key from the hashmap.

        Args:
            key (Union[str, int]): The key of the pair to be removed.

        Returns:
            bool: True if the pair was removed, False if the key was not found.
        """
        if not key:
            raise ValueError('key must not be None or empty.')

        if not isinstance(key, (str, int)):
            raise TypeError('key must be an instance of str or int.')

        index = self._hash(key)

        if self.hashmap[index] is None:
            return False

        for i, (existing_key, _) in enumerate(self.hashmap[index]):
            if existing_key == key:
                del self.hashmap[index][i]
                return True

        return False

    def keys(self) -> List[Union[str, int]]:
        """
        Returns a list of all the keys in the hashmap.

        Returns:
            List[Union[str, int]]: A list of all the keys in the hashmap.
        """
        key_list = []
        for bucket in self.hashmap:
            if bucket is not None:
                key_list.extend([key for key, _ in bucket])
        return key_list
