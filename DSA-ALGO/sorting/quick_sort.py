

# quick sort with random pivot

# Best              O(n*logn)
# Worst	            O(n^2)
# Average	        O(n*logn)
# Space Complexity	O(logn) for best, worst, average
# Stability	        No


import random


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]

    lower_list = []
    higher_list = []

    for item in arr:
        if item < pivot:
            lower_list.append(item)
        else:
            higher_list.append(item)

    sorted_list = quick_sort(lower_list) + quick_sort(higher_list)
    print('Sorted array:', sorted_list)
    return sorted_list


if __name__ == '__main__':
    print(quick_sort([1, 30, 6, 45, 7, 3, 2, 38]))
