# def peak_ele (arr):
#     #naive: take O(n) by looping through each element and check its neighbor, space O(1)
#     result = 0
    # if len(arr) == 1:
    #     return arr[0]
#     for i in range(len(arr)):    
#         if i != 0 and i != len(arr)-1:
#             if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
#                 result = arr[i]
#         else: 
#             if arr[i] == arr[0]:
#                 if arr[i] >= arr[i + 1]:
#                     result = arr[i]
                    
#             if arr[i] == arr[-1]:
#                 if arr[i] >= arr[i - 1]:
#                     result = arr[i]
#     return result


def peak_ele (arr):
    # time O(log n) || space: O(1)
    result = 0
    
    if len(arr) == 1:
        return arr[0]

    middle = len(arr)//2
    element = []
    element.append(middle)
    while element:
        curr = element.pop()
        if curr != 0 and curr != len(arr)-1: 
            if arr[curr] >= arr[curr - 1] and arr[curr] >= arr[curr + 1]:
                result = arr[curr]
                return result
                
        else: 
            if arr[curr] == arr[0]:
                if arr[curr] >= arr[curr + 1]:
                    result = arr[curr]
                    
            if arr[curr] == arr[-1]:
                if arr[curr] >= arr[curr - 1]:
                    result = arr[curr]
                    
            return result
            
        if arr[curr + 1] > arr[curr]:
            element.append(curr + 1)
        
        elif arr[curr - 1] > arr[curr]:
            element.append(curr - 1)
                    
        
    return result
    
    

if __name__ == '__main__':
    arr = [ 1, 3, 20, 4, 1, 0 ]
    
    print(peak_ele(arr))