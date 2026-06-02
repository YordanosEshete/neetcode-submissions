class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            current_price = prices[i]
            pot_profit = current_price - buy
            if pot_profit > max_profit:
                max_profit = pot_profit
        
        return max_profit
           
            



        