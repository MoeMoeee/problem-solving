class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False    
        
        print(sorted(s))

        return sorted(s) == sorted(t)
            

    
if __name__ == '__main__':
    a = Solution()
    print(a.isAnagram("rat", "car"))