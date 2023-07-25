class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        
        if len(cleaned_s) == 1 or len(cleaned_s) == 0:
            return True

        pointer1 = 0
        pointer2 = len(cleaned_s) - 1

        while pointer1 < pointer2:
            if cleaned_s[pointer1] != cleaned_s[pointer2]:
                return False
            
            pointer1 += 1
            pointer2 -= 1

        return True

        return True

            
        
    
if __name__ == '__main__':
    a = Solution()
    s = "..,"
    print(a.isPalindrome(s))


