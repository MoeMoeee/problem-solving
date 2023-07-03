# class Solution:
    # def groupAnagrams(self, strs):
    ### TLE since this is O(n^2)
    #     result = []
    #     check_lst = [0 for word in strs]

        
    #     if len(strs) == 1:
    #         return [strs]
    
        
    #     for i in range(len(strs)):
    #         temp = []
            
    #         if check_lst[i] > 0:
    #             continue
            
    #         sorted_word = sorted(strs[i])
    #         if  check_lst[i] == 0:
    #             temp.append(strs[i])
    #             check_lst[i] += 1
                
    #         for j in range(i+1, len(strs)):
    #             if check_lst[j] > 0:
    #                 continue
                
    #             next_sorted_word = sorted(strs[j])
    #             if sorted_word == next_sorted_word and check_lst[j] == 0 :
    #                 temp.append(strs[j])
    #                 check_lst[j] += 1
                    
    #         if len(temp) > 0:
    #             result.append(temp)
                
    #     return result
class Solution:
    def groupAnagrams(self, strs):
        # O(n*m*log(m) where n is the length of the list and m is the longest words)
        groups = {}
        temp = []
        result = []
        
        for i in range(len(strs)): 
            sorted_word = tuple(sorted(strs[i]))

            if sorted_word not in groups:
                groups[sorted_word] = [i]
            else:
                groups[sorted_word].append(i)
            
        for values in groups.values():
            temp = []
            for value in values:
                temp.append(strs[value])
            result.append(temp)
        return result
            
            
        
if __name__ == '__main__':
    a = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(a.groupAnagrams(strs))