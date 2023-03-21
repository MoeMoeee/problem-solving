def merge_sorted(arr1, arr2):
    result = []
    item_1 = arr1[0]
    item_2 = arr2[0]
    index_1 = 0
    index_2 = 0
    bool_1 = False
    bool_2 = False

    while (not bool_1 or not bool_2):
        # check to not out of range
        if index_1 == len(arr1):
            bool_1 = True
        else:
            item_1 = arr1[index_1]

        # check to not out of range
        if index_2 == len(arr2):
            bool_2 = True
        else:
            item_2 = arr2[index_2]

        if not bool_1 and (bool_2 or item_1 < item_2):
            result.append(item_1)
            index_1 += 1
        elif not bool_2 and (bool_1 or item_1 >= item_2):
            result.append(item_2)
            index_2 += 1

    return result


if __name__ == "__main__":
    print(merge_sorted([1, 4, 4, 6], [2, 4, 8, 9, 11]))
    # => [1, 4, 4, 4, 6, 8, 9]
