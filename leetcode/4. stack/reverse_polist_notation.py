
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def is_operator(self, s):
            return s in ["+", "-", "*", "/"]
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if not self.is_operator(i): # add to stack if num
                stack.append(i)
            else:
                if len(stack) >= 2:
                    # do operation when we got an operator
                    num1, num2 = stack.pop(), stack.pop()
                    newVal = self.getVal(int(num1), int(num2), i)
                    stack.append(str(newVal))
        return int(stack.pop())
            
    def getVal(self, num1: int, num2: int, str: str) -> int:
        if str == "+":
            return num2 + num1
        elif str == "-":
            return num2 - num1
        elif str == "*":
            return num2 * num1
        elif str == "/":
            return int(num2 / num1)


if __name__ == '__main__':
    a = Solution()
    token = ["4","13","5","/","+"]
    print(a.evalRPN(token))