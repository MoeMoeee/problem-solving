# non repeated substring of length 3
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        LENGTH_GOOD_SUBSTRING = 3
        counter = 0
        
        for i in range(len(s)):
            next_id = LENGTH_GOOD_SUBSTRING + i
            curr_sub = s[i:next_id]

            if (len(set(curr_sub)) == LENGTH_GOOD_SUBSTRING):
                counter += 1

        return counter
            

            



        