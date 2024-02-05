class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        window_min = prices[0]
        
        for price in prices:
            window_min = min(window_min, price)
            max_profit = max(max_profit, price - window_min)

        return max_profit

    





        
            
        

        
if __name__ == '__main__':
    a = Solution()
    arr = [[0,1,0,0,0],
            [1,1,1,0,0],
            [1,1,0,0,0],
            [0,1,0,1,0]]
    print(a.sol(arr, 1,2,2))

        
        




# if __name__ == '__main__':
#     a = Solution()
#     prices = [7,1,5,3,6,4]
#     print(a.maxProfit(prices))
    
    