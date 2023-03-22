

# quick sort with random pivot

# Best              O(n*logn)
# Worst	            O(n^2)
# Average	        O(n*logn)
# Space Complexity	O(logn) for best, worst, average
# Stability	        No

# def partition(arr, start, end):
#     # choose a random pivot index
#     pivot_index = random.randint(start, end)

#     # swap the pivot element with the last element
#     arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

#     # set the pivot as the last element
#     pivot = arr[end]

#     # partition the array
#     i = start - 1
#     for j in range(start, end):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[end] = arr[end], arr[i+1]
#     return i+1

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
