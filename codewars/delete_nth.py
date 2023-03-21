
def delete_nth(lst, max):
    result = []
    count = {}

    for item in lst:
        if item not in count:
            count[item] = 0
        if count[item] < max:
            result.append(item)
            count[item] += 1

    return result


if __name__ == '__main__':
    print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
