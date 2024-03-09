class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def recursion(openParen, closeParen, par):
            
            if openParen == closeParen == n:
                result.append(par)
                return
            
            if openParen < n:
                recursion(openParen + 1, closeParen, par+'(')
                
            if openParen > closeParen:
                recursion(openParen, closeParen + 1, par+')')      
            
        recursion(0, 0, '')
        return result