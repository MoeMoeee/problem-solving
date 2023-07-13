class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        lst = []
        
        for i in range(len(strs)):
            lst.append(strs[i])
            
            if i < len(strs):
                lst.append(",")
                
        return "".join(lst)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        lst = []
        empty_str = ""

        
        for i in str:
            if i != ',':
                empty_str += i
            else:
                lst.append(empty_str)
                empty_str = "" # reset the string
                
        return lst

        
        
if __name__ == '__main__':
    a = Solution()
    input = ["lint","code","love","you"]
    encode = a.encode(input)
    # print(encode)       
    print(a.decode(encode))        
     