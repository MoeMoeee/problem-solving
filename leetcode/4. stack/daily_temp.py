# https://leetcode.com/problems/daily-temperatures/description/

from typing import List


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0]*(len(temperatures))
#         stack = []
        



#         for i in range(len(temperatures)-1, 0, -1):
#             if i == 0 and temperatures[i] > temperatures[i+1]:
#                 res[0] = 1
                
#             if(temperatures[i] > temperatures[i-1] and i != 0): 
#                 stack.append(i)
#                 res[i-1] = 1
#             else:
#                 for j in stack:
#                     curr_i = stack.pop()
#                     if temperatures[i-1] < temperatures[curr_i]:
#                         res[i-1] = abs(curr_i - i) + 1

#         return res
    
    
    
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res


if __name__ == '__main__':
    a = Solution()
    token = [73,74,75,71,69,72,76,73]
    print(a.dailyTemperatures(token))