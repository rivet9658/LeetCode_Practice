# package import
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        earn = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                earn = max(earn, sell - buy)
            else:
                buy = sell
        return earn
