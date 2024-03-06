
# https://leetcode.com/problems/permutation-in-string/description/

class Solution(object):
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        - return true if s1 per in s2
        """
        # 1st attempt - TLE 
        # O(s1*s2) = O(n^2)
        # to_check = len(s1)
        
        # for i in range(len(s2)):
        #     curr = s2[i:i+to_check]
        #     if sorted(s1) == sorted(curr):
        #         return True
        
        # return False


        # 2nd - passed but 
        # still O(mn)

        to_check = len(s1)
        sorted_s1 = sorted(s1)
        
        
        for i in range(len(s2)):
            curr = s2[i:i+to_check]
            if sorted_s1 == sorted(curr):
                return True
        
        return False
        
            
        

        
if __name__ == '__main__':
    a = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    print(a.checkInclusion(s1, s2)) # True
    
    
    s1 = "ab"
    s2 = "eidboaoo"
    print(a.checkInclusion(s1, s2)) #False

        
        




# if __name__ == '__main__':
#     a = Solution()
#     prices = [7,1,5,3,6,4]
#     print(a.maxProfit(prices))
    
    