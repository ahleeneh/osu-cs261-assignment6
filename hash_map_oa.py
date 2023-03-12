# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

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
        Increment from given number to find the closest prime number
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
        if self.table_load() >= 0.5:
            self.resize_table(self._capacity * 2)

        entry, probe_i = self._quadratic_probe_insert(key)
        if entry is None or entry.is_tombstone:
            self._buckets[probe_i] = HashEntry(key, value)
            self._size += 1
        else:
            # replace contents of a hash entry that already exists in the map
            entry.value = value
            entry.is_tombstone = False

    def table_load(self) -> float:
        """
        Determine the load factor of the HashMap.

        :return float: current HashMap load factor
        """
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """
        Determine the number of empty buckets in the HashMap.

        :return int: quantity of empty buckets in the HashMap
        """
        return self._capacity - self._size

    def resize_table(self, new_capacity: int) -> None:
        """
        Resize the HashMap and rehash all the existing key/value pairs.

        :param new_capacity: capacity to resize HashMap to
        """
        if new_capacity >= self._size:
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

    def get(self, key: str) -> object:
        """
        Determine the value associated with the specified key.

        :param key: key to find in a HashMap
        :return object: value associated with the specified key
        """
        entry = self._quadratic_probe_search(key)
        if entry is None or entry.is_tombstone:
            return None
        return entry.value

    def contains_key(self, key: str) -> bool:
        """
        Determine if the value associated with the specified key exists in a
        HashMap.

        :param key: key to find in a HashMap
        :return bool: True if key found in HashMap; false, otherwise.
        """
        entry = self._quadratic_probe_search(key)
        if entry is None or entry.is_tombstone:
            return False
        return True

    def remove(self, key: str) -> None:
        """
        Remove the specified key and its associated value from a HashMap.

        :param key: key to find in a HashMap to delete key/value pair
        """
        entry = self._quadratic_probe_search(key)
        if entry and entry.key == key and entry.is_tombstone is False:
            entry.is_tombstone = True
            self._size -= 1

    def clear(self) -> None:
        """
        Clear the contents of the HashMap.
        """
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append(None)
        self._size = 0

    def get_keys_and_values(self) -> DynamicArray:
        """
        Create a new DynamicArray object where each index contains a tuple of
        all key/value pair stored in a HashMap.

        :return DynamicArray: contains the key/value pairs stored in a HashMap
        """
        hashmap = DynamicArray()
        for entry in self:
            hashmap.append((entry.key, entry.value))
        return hashmap

    def __iter__(self):
        """
        Initialize new Hashmap.
        """
        return HashMapIterator(self._buckets)

    def _quadratic_probe_insert(self, key: object) -> (HashEntry, int):
        """
        Helper method for put() - perform quadratic probing until the hash
        entry or an empty spot/hash entry with a tombstone value is found.

        :param key: key to find in a HashMap
        :return tuple: specified key's corresponding HashEntry and index
        """
        initial_i, j = self._hash_function(key) % self._capacity, 0
        probe_i = (initial_i + j ** 2) % self._capacity
        entry = self._buckets[probe_i]

        while entry and entry.key != key and not entry.is_tombstone:
            j += 1
            probe_i = (initial_i + j ** 2) % self._capacity
            entry = self._buckets[probe_i]
        return entry, probe_i

    def _quadratic_probe_search(self, key: object) -> HashEntry:
        """
        Helper method for contains_key() and get() - perform quadratic probing
        until the hash entry or an empty spot is found.

        :param key: key to find in a HashMap
        :return HashEntry: specified key's corresponding HashEntry
        """
        initial_i, j = self._hash_function(key) % self._capacity, 0
        probe_i = (initial_i + j ** 2) % self._capacity
        entry = self._buckets[probe_i]

        while entry is not None and entry.key != key:
            j += 1
            probe_i = (initial_i + j ** 2) % self._capacity
            entry = self._buckets[probe_i]
        return entry


# ---------------------------------------------------------------------- #


class HashMapIterator:
    def __init__(self, map_da: DynamicArray):
        """
        Init new Hashmap iterator and index based on a DynamicArray.

        :param map_da: DynamicArray object.
        """
        self._idx = 0
        self._map = map_da

    def __iter__(self):
        """
        :return: iterator object itself
        """
        return self

    def __next__(self):
        """
        Obtain the next active value and advance iterator.

        :return: next element in the sequence
        """
        if self._idx >= self._map.length():
            raise StopIteration

        node, size = self._map[self._idx], self._map.length() - 1
        while (node is None and self._idx < size) or (node and node.is_tombstone):
            self._idx += 1
            node = self._map[self._idx]

        if node is not None:
            self._idx += 1
            return node
        raise StopIteration

