from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        group = defaultdict(int)
        
        
        for num in nums:
            group[num] += 1
            
        sorted_values = sorted(group.values(), reverse = True)
        
        k_element = sorted_values[:k]
        
        
        for key in group.keys():
            if group[key] in k_element:
                result.append(key)
        return result

        
        
if __name__ == '__main__':
    a = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(a.topKFrequent(nums, k))        