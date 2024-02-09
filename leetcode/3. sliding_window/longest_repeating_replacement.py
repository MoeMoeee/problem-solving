from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ######################################################################################################
        # FIRST ATTEMPT
        # if not s:
        #     return 0

        # longest_sub = 1
        # most_repeated_char = s[0]
        # temp = 1
        # pointer = 1
        # temp_k = k

        # while pointer < len(s):
        #     if s[pointer] == most_repeated_char:
        #         temp += 1
        #     else:
        #         if temp_k > 0:
        #             temp_k -= 1
        #             temp += 1
        #         else:
        #             temp_k = k
        #             most_repeated_char = s[pointer]  # Update most_repeated_char based on the new substring
        #             temp = 1 + temp - (temp_k + 1)  # Subtract the count of characters between old and new most_repeated_char

        #     longest_sub = max(longest_sub, temp)
        #     pointer += 1

        # return longest_sub
        
        
        
        


        ######################################################################################################


        count = longest_substring = start = 0
        tracking = defaultdict(int)
        

        for i in range(len(s)):
            tracking[s[i]] += 1
            
            count = max(count, tracking[s[i]]) #max current count 
            
            # mean there is a mixmatch > number to swap
            if i - start + 1 - count > k:
                tracking[s[start]] -=  1
                start += 1 
                
            # i - start + 1 = curr valid substring
            longest_substring = max(longest_substring, i - start + 1)

        return longest_substring


if __name__ == '__main__':
    a = Solution()
    s = "BBAAAA"
    k = 2
    print(a.characterReplacement(s, k))