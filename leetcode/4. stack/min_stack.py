# https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:   
        stack = self.stack

        curr_min = val
            
        
        if len(stack) > 0:
            if val >= self.getMin():
                curr_min = self.getMin()
            
        
        stack.append([val, curr_min])
        
        
    def pop(self) -> None:
        stack = self.stack
        stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        

        
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) 
    minStack.pop();
    print(minStack.top())
    print(minStack.getMin()) 
    
    
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    