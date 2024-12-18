class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new_prices = []
        for i in range(len(prices)):
            price = prices[i]
            discount_applied = False
            for discount in prices[i+1:]:
                if price >= discount:
                    new_prices.append(price - discount)
                    discount_applied = True
                    break
                else:
                    continue
            if not discount_applied:
                new_prices.append(price)
        return new_prices