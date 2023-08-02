class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        TLE 
        """
        
        # pointer1 = 0
        # result = []
        # while pointer1 < len(numbers):
            
        #     pointer2 = pointer1 + 1
        #     while pointer2 < len(numbers):
        #         if numbers[pointer1] + numbers[pointer2] == target:
        #             result.append(pointer1+1)
        #             result.append(pointer2+1)
        #             return result
                    
        #         pointer2 += 1
        #     pointer1 += 1
    
                
        pointer1 = 0
        result = []
        while pointer1 < len(numbers):
            
            pointer2 = self.binarySearch(target - numbers[pointer1], pointer1 + 1, numbers)
            if pointer2 != -1:
                result.append(pointer1+1)
                result.append(pointer2+1)
                return result
            pointer1 += 1
                    
        
        
    def binarySearch(self, target, low, numbers):
        high = len(numbers) - 1
        
        while low <= high:
            mid = (high+low) // 2
            
            if numbers[mid] < target:
                low = mid + 1
    
            elif numbers[mid] > target:
                high = mid - 1
            
            else:
                return mid 
        return -1
        
    
if __name__ == '__main__':
    a = Solution()
    numbers = [-1 , 0]
    target = -1

    print(a.twoSum(numbers, target))


