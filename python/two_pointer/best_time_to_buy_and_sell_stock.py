'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def maxProfit(prices):
    length = len(prices)
    if length in (1,0):
        return 0
    i = 0
    j = 1
    result = 0
    while j<length:
        pl = prices[j]-prices[i]
        if pl>0:
            result = max(result,pl)
            j+=1
        else:
            i+=1
            if i==j:
                j+=1
    return result

result = maxProfit([7,1,5,3,6,4])
print(result) # 5
result = maxProfit([7,6,4,3,1])
print(result) # 0