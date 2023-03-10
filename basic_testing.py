# ------------------- BASIC TESTING ---------------------------------------- #

# if __name__ == "__main__":

    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(53, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(41, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(101, hash_function_1)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(53, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(101, hash_function_1)
    # print(round(m.table_load(), 2))
    # m.put('key1', 10)
    # print(round(m.table_load(), 2))
    # m.put('key2', 20)
    # print(round(m.table_load(), 2))
    # m.put('key1', 30)
    # print(round(m.table_load(), 2))
    #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(53, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(round(m.table_load(), 2), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(101, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.get_size(), m.get_capacity())
    # m.resize_table(100)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())
    # #
    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(23, hash_function_1)
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    # #
    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(79, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.get_size(), m.get_capacity())
    # #
    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)
    #
    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')
    #
    #     for key in keys:
    #         # all inserted keys must be present
    #         result &= m.contains_key(str(key))
    #         # NOT inserted keys must be absent
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(31, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(151, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.get_size(), m.get_capacity())
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(79, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.get_size(), m.get_capacity())
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')
    #
    # print("\nPDF - get_keys_and_values example 1")
    # print("------------------------")
    # m = HashMap(11, hash_function_2)
    # for i in range(1, 6):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys_and_values())
    #
    # m.put('20', '200')
    # m.remove('1')
    # m.resize_table(2)
    # print(m.get_keys_and_values())

    # print("\nPDF - find_mode example 1")
    # print("-----------------------------")
    # da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    # mode, frequency = find_mode(da)
    # print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    # print("\nPDF - find_mode example 2")
    # print("-----------------------------")
    # test_cases = (
    #     ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
    #     ["one", "two", "three", "four", "five"],
    #     ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    # )
    #
    # for case in test_cases:
    #     da = DynamicArray(case)
    #     mode, frequency = find_mode(da)
    #     print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")






# ------------------- BASIC TESTING ---------------------------------------- #
#
# if __name__ == "__main__":
#
#     print("\nPDF - put example 1")
#     print("-------------------")
#     m = HashMap(53, hash_function_1)
#     for i in range(150):
#         m.put('str' + str(i), i * 100)
#         if i % 25 == 24:
#             print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
#
#     print("\nPDF - put example 2")
#     print("-------------------")
#     m = HashMap(41, hash_function_2)
#     for i in range(50):
#         m.put('str' + str(i // 3), i * 100)
#         if i % 10 == 9:
#             print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
#     #
#     print("\nPDF - table_load example 1")
#     print("--------------------------")
#     m = HashMap(101, hash_function_1)
#     print(round(m.table_load(), 2))
#     m.put('key1', 10)
#     print(round(m.table_load(), 2))
#     m.put('key2', 20)
#     print(round(m.table_load(), 2))
#     m.put('key1', 30)
#     print(round(m.table_load(), 2))
#
#     print("\nPDF - table_load example 2")
#     print("--------------------------")
#     m = HashMap(53, hash_function_1)
#     for i in range(50):
#         m.put('key' + str(i), i * 100)
#         if i % 10 == 0:
#             print(round(m.table_load(), 2), m.get_size(), m.get_capacity())
#
#     print("\nPDF - empty_buckets example 1")
#     print("-----------------------------")
#     m = HashMap(101, hash_function_1)
#     print(m.empty_buckets(), m.get_size(), m.get_capacity())
#     m.put('key1', 10)
#     print(m.empty_buckets(), m.get_size(), m.get_capacity())
#     m.put('key2', 20)
#     print(m.empty_buckets(), m.get_size(), m.get_capacity())
#     m.put('key1', 30)
#     print(m.empty_buckets(), m.get_size(), m.get_capacity())
#     m.put('key4', 40)
#     print(m.empty_buckets(), m.get_size(), m.get_capacity())
#
#     print("\nPDF - empty_buckets example 2")
#     print("-----------------------------")
#     m = HashMap(53, hash_function_1)
#     for i in range(150):
#         m.put('key' + str(i), i * 100)
#         if i % 30 == 0:
#             print(m.empty_buckets(), m.get_size(), m.get_capacity())
#
#     print("\nPDF - resize example 1")
#     print("----------------------")
#     m = HashMap(23, hash_function_1)
#     m.put('key1', 10)
#     print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
#     m.resize_table(30)
#     print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
#
#     print("\nPDF - resize example 2")
#     print("----------------------")
#     m = HashMap(79, hash_function_2)
#     keys = [i for i in range(1, 1000, 13)]
#     for key in keys:
#         m.put(str(key), key * 42)
#     print(m.get_size(), m.get_capacity())
#
#     for capacity in range(111, 1000, 117):
#         m.resize_table(capacity)
#
#         if m.table_load() > 0.5:
#             print(f"Check that the load factor is acceptable after the call to resize_table().\n"
#                   f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")
#
#         m.put('some key', 'some value')
#         result = m.contains_key('some key')
#         m.remove('some key')
#
#         for key in keys:
#             # all inserted keys must be present
#             result &= m.contains_key(str(key))
#             # NOT inserted keys must be absent
#             result &= not m.contains_key(str(key + 1))
#         print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))
#
#     print("\nPDF - get example 1")
#     print("-------------------")
#     m = HashMap(31, hash_function_1)
#     print(m.get('key'))
#     m.put('key1', 10)
#     print(m.get('key1'))
#     #
#     print("\nPDF - get example 2")
#     print("-------------------")
#     m = HashMap(151, hash_function_2)
#     for i in range(200, 300, 7):
#         m.put(str(i), i * 10)
#     print(m.get_size(), m.get_capacity())
#     for i in range(200, 300, 21):
#         print(i, m.get(str(i)), m.get(str(i)) == i * 10)
#         print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
#
#     print("\nPDF - contains_key example 1")
#     print("----------------------------")
#     m = HashMap(11, hash_function_1)
#     print(m.contains_key('key1'))
#     m.put('key1', 10)
#     m.put('key2', 20)
#     m.put('key3', 30)
#     print(m.contains_key('key1'))
#     print(m.contains_key('key4'))
#     print(m.contains_key('key2'))
#     print(m.contains_key('key3'))
#     m.remove('key3')
#     print(m.contains_key('key3'))
#
#     print("\nPDF - contains_key example 2")
#     print("----------------------------")
#     m = HashMap(79, hash_function_2)
#     keys = [i for i in range(1, 1000, 20)]
#     for key in keys:
#         m.put(str(key), key * 42)
#     print(m.get_size(), m.get_capacity())
#     result = True
#     for key in keys:
#         # all inserted keys must be present
#         result &= m.contains_key(str(key))
#         # NOT inserted keys must be absent
#         result &= not m.contains_key(str(key + 1))
#     print(result)
#
#     print("\nPDF - remove example 1")
#     print("----------------------")
#     m = HashMap(53, hash_function_1)
#     print(m.get('key1'))
#     m.put('key1', 10)
#     print(m.get('key1'))
#     m.remove('key1')
#     print(m.get('key1'))
#     m.remove('key4')
#
#     print("\nPDF - clear example 1")
#     print("---------------------")
#     m = HashMap(101, hash_function_1)
#     print(m.get_size(), m.get_capacity())
#     m.put('key1', 10)
#     m.put('key2', 20)
#     m.put('key1', 30)
#     print(m.get_size(), m.get_capacity())
#     m.clear()
#     print(m.get_size(), m.get_capacity())
#
#     print("\nPDF - clear example 2")
#     print("---------------------")
#     m = HashMap(53, hash_function_1)
#     print(m.get_size(), m.get_capacity())
#     m.put('key1', 10)
#     print(m.get_size(), m.get_capacity())
#     m.put('key2', 20)
#     print(m.get_size(), m.get_capacity())
#     m.resize_table(100)
#     print(m.get_size(), m.get_capacity())
#     m.clear()
#     print(m.get_size(), m.get_capacity())
#
#     print("\nPDF - get_keys_and_values example 1")
#     print("------------------------")
#     m = HashMap(11, hash_function_2)
#     for i in range(1, 6):
#         m.put(str(i), str(i * 10))
#     print(m.get_keys_and_values())
#     #
#     m.resize_table(2)
#     print(m.get_keys_and_values())
#
#     m.put('20', '200')
#     m.remove('1')
#     m.resize_table(12)
#     print(m.get_keys_and_values())
#
#     print("\nPDF - __iter__(), __next__() example 1")
#     print("---------------------")
#     m = HashMap(10, hash_function_1)
#     for i in range(5):
#         m.put(str(i), str(i * 10))
#     print(m)
#     for item in m:
#         print('K:', item.key, 'V:', item.value)
#
#     print("\nPDF - __iter__(), __next__() example 2")
#     print("---------------------")
#     m = HashMap(10, hash_function_2)
#     for i in range(5):
#         m.put(str(i), str(i * 24))
#     m.remove('0')
#     m.remove('4')
#     print(m)
#     for item in m:
#         print('K:', item.key, 'V:', item.value)
