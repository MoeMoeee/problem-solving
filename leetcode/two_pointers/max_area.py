class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start, end = 0, len(height) - 1
        max_vol = 0

        while start < end:
            # Calculate the current volume
            current_vol = min(height[start], height[end]) * (end - start)

            # Update the max volume if the current one is greater
            max_vol = max(max_vol, current_vol)

            # Move the pointers based on the height of the walls
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_vol

        
        
        
if __name__ == '__main__':
    a = Solution()
    height = [1,2,4,3]
    print(a.maxArea(height))