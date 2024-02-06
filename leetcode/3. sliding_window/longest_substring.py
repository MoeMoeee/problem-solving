from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        need to realize when to reset the pointer 
        -> reset the pointer back to the repeated char
        -> keep track of the postion using dict
        """
        
        curr_longest, all_time = 0, 0
        start, pointer = 0, 0
        dict_tracking = defaultdict(int)
        
        while pointer < len(s):

            curr_char = s[pointer]
            
            if dict_tracking[curr_char] > 0:  # repeat
                start = max(start, dict_tracking[curr_char])
                dict_tracking[curr_char] = pointer + 1
                curr_longest = pointer - start + 1
                
            else:
                curr_longest += 1
                dict_tracking[curr_char] = pointer + 1
                
            if curr_longest > all_time:
                all_time = curr_longest
            
            pointer += 1  # Move the pointer forward

        return all_time

if __name__ == '__main__':
    a = Solution()
    str = "abcad"
    print(a.lengthOfLongestSubstring(str))