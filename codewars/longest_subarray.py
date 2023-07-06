def maxLength(a, k):
    # Write your code here
    result = 0
    i = 0
    next_i = 0
    sub_arrays = []
    curr_sum = 0
    max_length = 0
    while i < len(a):
        curr_sum += a[i]
        
        while curr_sum > k:
            curr_sum -= a[next_i]
            next_i += 1
            
        if curr_sum <= k:
            curr_length = i - next_i + 1
            print(curr_length)
            if curr_length > max_length:
                sub_arrays = []
                sub_arrays.append(a[next_i:i + 1])
                max_length = curr_length
            
        i+=1
        
    return sub_arrays

if __name__ == '__main__':
    a = [5,5,1,3]
    k = 4
    print(maxLength(a, k))