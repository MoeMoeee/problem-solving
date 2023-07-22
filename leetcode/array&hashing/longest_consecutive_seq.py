class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        
        num_set = set(nums)
        longest_consecutive = []
        curr_val = 0
        
        for i in num_set:
            if i-1 not in num_set:
                curr_val = i
                longest_consecutive.append(1)
                
                while True:
                    if curr_val + 1 in num_set:
                        longest_consecutive.append(longest_consecutive[-1] + 1)
                        curr_val += 1
                    else:                        
                        break

        return max(longest_consecutive)
                    
    
if __name__ == '__main__':
    a = Solution()
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    print(a.longestConsecutive(nums))


