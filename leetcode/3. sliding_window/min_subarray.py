# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=list&envId=xlep8di5

# return length of min sub array can construct >= target, else 0 


from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2 = 0, 0
        curr_sum = 0
        res = float('inf')  # Initialize result to positive infinity

        while p2 < len(nums):
            curr_sum += nums[p2]

            while curr_sum >= target:
                res = min(res, p2 - p1 + 1)
                curr_sum -= nums[p1]
                p1 += 1

            p2 += 1

        return res if res != float('inf') else 0

    
    
if __name__ == '__main__':
    a = Solution()
    print(a.minSubArrayLen(7, [2,3,1,2,4,3]))