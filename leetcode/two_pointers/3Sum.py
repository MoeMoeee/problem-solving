class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()
        start = 0
        result = set()
        end = len(nums) - 1

        while end > start:
            target = 0 - nums[start]
            pointer = start + 1

            while pointer < end:
                curr = nums[end] + nums[pointer]
                if curr > target:
                    end -= 1
                elif curr < target:
                    pointer += 1
                else:
                    temp = [nums[start], nums[pointer], nums[end]]
                    result.add(tuple(temp))
                    pointer += 1  # Increment pointer when triplet is found

            start += 1
            pointer = start + 1  # Reset pointer after incrementing start
            end = len(nums) - 1  # Reset end after incrementing start

        lstNum = [list(t) for t in result]
        return lstNum




if __name__ == '__main__':
    a = Solution()
    numbers = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(a.threeSum(numbers))
    
    
    #[[-3, -1, 4], [-1, 0, 1], [-4, 1, 3], [-2, 0, 2], [-1, -1, 2], [-3, 0, 3], [-4, 0, 4], [-2, -1, 3], [-3, 1, 2]]