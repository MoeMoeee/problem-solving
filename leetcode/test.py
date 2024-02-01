from math import floor

class MyBigNumber:
    
    def sum(self, str1: str, str2: str) -> str:
        sum_list = []
        carry = 0
        

        for i in range(1, max(len(str1), len(str2)) + 1):
            digit1, digit2 = 0, 0
            
            # Get digits 
            if i <= len(str1):
                digit1 = int(str1[-i])
                
            if i <= len(str2):
                digit2 = int(str2[-i])
            
            # Proceed to sum
            curr_sum = carry + digit1 + digit2
            
            carry = curr_sum // 10
            
            sum_list.append(str(curr_sum % 10))
            
        if carry:
            sum_list.append(str(carry))
            

        return ''.join(reversed(sum_list))

if __name__ == '__main__':
    a = MyBigNumber()
    print(a.sum("12", "21"))  
    print(a.sum("14", "151"))  
    print(a.sum("54", "951")) # edge case
