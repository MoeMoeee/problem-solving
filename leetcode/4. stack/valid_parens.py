# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        

        dict_paren = {
            '(': ')',
            '[': ']',
            '{': '}'
        }                                                              

        if len(s) % 2 != 0:
            return False
        
        for i in s:
            if i in dict_paren.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                curr = stack.pop()
                
                if dict_paren[curr] != i:
                    return False
        
        if len(stack) > 0:
            return False

        return True
        
            
        

        
if __name__ == '__main__':
    a = Solution()

    s = "()"
    print(a.isValid(s)) # True
    
    
    s = "()[]{}"
    print(a.isValid(s)) # True
    

    s = "()["
    print(a.isValid(s)) # False