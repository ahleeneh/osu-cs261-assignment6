# Name: Aline Murillo
# OSU Email: murilali@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: Mar-17-2023
# Description:


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Update or insert the key/value pair into the HashMap.

        :param key: key of key/value pair to put into a HashMap
        :param value: value of key/value pair to put into a HashMap
        """
        if self.table_load() >= 1:
            self.resize_table(self._capacity * 2)

        sll = self.get_sll(key)
        node = sll.contains(key)
        if node is not None:
            node.value = value
        else:
            sll.insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """
        Determine the number of empty buckets in the HashMap.

        :return int: quantity of empty buckets in the HashMap
        """
        tally = 0
        for i in range(self._capacity):
            if self._buckets[i].length() == 0:
                tally += 1
        return tally

    def table_load(self) -> float:
        """
        Determine the load factor of the HashMap.

        :return float: current HashMap load factor
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        Clear the contents of the HashMap.
        """
        self._buckets = DynamicArray()
        self._size = 0
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

    def resize_table(self, new_capacity: int) -> None:
        """
        Resize the HashMap and rehash all the existing key/value pairs.

        :param new_capacity: capacity to resize HashMap to
        """
        if new_capacity > 0:
            old_hashmap = self.get_keys_and_values()
            self.resize_table_capacity(new_capacity)
            self.clear()
            for i in range(old_hashmap.length()):
                k, v = old_hashmap[i]
                self.put(k, v)

    def resize_table_capacity(self, new_capacity: int) -> None:
        """
        Helper method for resize_table() - change the capacity of the HashMap.

        :param new_capacity: capacity to resize HashMap to
        """
        if self._is_prime(new_capacity):
            self._capacity = new_capacity
        else:
            self._capacity = self._next_prime(new_capacity)

    def get(self, key: str):
        """
        Determine the value associated with the specified key.

        :param key: key to find in a HashMap
        """
        node = self.get_sll(key).contains(key)
        if node is not None:
            return node.value
        return node

    def contains_key(self, key: str) -> bool:
        """
        Determine if the value associated with the specified key exists in a
        HashMap.

        :param key: key to find in a HashMap
        :return bool: True if key found in HashMap; false, otherwise.
        """
        node = self.get_sll(key).contains(key)
        if node is not None:
            return True
        return False

    def remove(self, key: str) -> None:
        """
        Remove the specified key and its associated value from a HashMap.

        :param key: key to find in a HashMap to delete key/value pair
        """
        sll = self.get_sll(key)
        if sll.length() > 0 and sll.remove(key):
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Create a new DynamicArray object where each index contains a tuple of
        all key/value pair stored in a HashMap.

        :return DynamicArray: contains the key/value pairs stored in a HashMap
        """
        hashmap = DynamicArray()
        for i in range(self._capacity):
            sll = self._buckets[i]
            if sll.length() > 0:
                for node in sll:
                    hashmap.append((node.key, node.value))
        return hashmap

    def get_sll(self, key: str) -> LinkedList:
        """
        Helper method for put(), get(), contains_key(), remove() - determine
        the singly linked list associated with the specified key in a HashMap.

        :param key: key to find in a HashMap to find its singly linked list
        :return LinkedList: a key's corresponding singly linked list
        """
        key_index = self._hash_function(key) % self._capacity
        return self._buckets[key_index]


# ---------------------------------------------------------------------- #


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Create a new DynamicArray object that contains the mode values of a
    DynamicArray and determine the highest frequency of a DynamicArray.

    :param da: DynamicArray to find mode from
    :return tuple: DynamicArray that contains mode values and mode frequency
    """
    map, mode_da, mode_frequency = HashMap(), DynamicArray(), 0

    for i in range(da.length()):
        # determine frequency of item in array and add key/value pair to map
        value = find_mode_helper(map, da[i])

        # add mode to new dynamic array
        if value >= mode_frequency:
            if value > mode_frequency:
                mode_da = DynamicArray()
                mode_frequency = value
            mode_da.append(da[i])

    return mode_da, mode_frequency


def find_mode_helper(map: HashMap, key) -> int:
    """
    Helper method for find_mode() - add or update the key/value pair with the
    associated key in HashMap.

    :param map: HashMap to add or update key/value pair to
    :param key: key to find in a HashMap to add or update key/value pair
    :return int: temporary frequency of a specified key
    """
    value = map.get(key)
    if value is not None:
        value += 1
    else:
        value = 1
    map.put(key, value)
    return value

