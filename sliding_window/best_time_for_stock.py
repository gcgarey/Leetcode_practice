def maxProfit(prices):
    res = 0
    b, s = 0, 1
    while s < len(prices):
        
        profit = prices[s] - prices[b]
        res = max(res, profit)

        if prices[s] < prices[b]:
            prices[b] = prices[s]

        s += 1

    return res


        