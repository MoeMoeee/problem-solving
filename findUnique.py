def find_uniq(arr):
    uniqueList = set(arr)  # simplfy the list by not allowing duplicate
    uniqueNumber = 0

    min = arr.count(arr[0])

    for item in uniqueList:
        if arr.count(item) < min:  # find the min occurence -> the unique number
            uniqueNumber = item
            min = arr.count(item)

    return uniqueNumber


if __name__ == "__main__":
    print(find_uniq([1, 1, 1, 2, 1, 1]))
    print(find_uniq([0, 0, 0.55, 0, 0]))
    print(find_uniq([3, 10, 3, 3, 3]))
