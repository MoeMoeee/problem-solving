# Counting sort is a sorting algorithm that sorts the elements of an array by counting the
# number of occurrences of each unique element in the array.

# Time Complexity
# Best	            O(n+u)  (u is size)
# Worst	            O(n+u)
# Average	        O(n+u)
# Space Complexity	O(n+u) for best, worst, average
# Stability	        Yes

def counting_sort(arr, size):
    # first create the result list to hold using the given size
    result = [0]*len(arr)
    counter_arr = [0]*(size+1)  # temp to count the occurrences

    # find the occurrences of each element
    for i in range(0, len(arr)):
        ele = arr[i]
        counter_arr[ele] += 1
        # counter_arr = [0, 1, 2, 1, 0, 1, 0, 1, 0, 1]

    # increment the occurrences
    for i in range(1, len(counter_arr)):
        counter_arr[i] = counter_arr[i-1] + counter_arr[i]
        # [0, 1, 3, 4, 4, 5, 5, 6, 6, 7]

    for i in range(len(arr)):
        element = arr[i]
        temp_index = counter_arr[element]
        # temp_index - 1 because array index starts from 0
        result[temp_index-1] = element
        counter_arr[element] -= 1

    return result


if __name__ == "__main__":
    arr = [0, 3, 2, 5, 1, 2, 7, 9]
    max_val = max(arr)
    print(counting_sort(arr, max_val))
