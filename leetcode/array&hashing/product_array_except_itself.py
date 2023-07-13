class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        answer = [0]*len(nums)
        accu = 1
        
        for i in range(len(nums)):
            left_prod[i] = accu * nums[i]
            accu = left_prod[i]
        
        accu = 1
        
        for j in reversed(range(len(nums))):
            right_prod[j] = accu * nums[j]
            accu = right_prod[j]
        
        for k in range(len(answer)):
            if k == 0: #edge 
                answer[k] = right_prod[k+1]
            
            elif k == len(answer)-1: #edge
                answer[k] = left_prod[k-1]
                
            else:
                answer[k] = right_prod[k+1] * left_prod[k-1]
        
        return answer
if __name__ == '__main__':
    a = Solution()
    nums = [-1,1,0,-3,3]
    print(a.productExceptSelf(nums))


