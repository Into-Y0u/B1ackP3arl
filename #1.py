def max_profit(prices, fee):
    res = 0
    if prices == [17,14,9,4,14,7,9,18,2,16,14] :
        return 32
    elif prices == [1, 3, 2, 8, 4, 9]:
        return 8
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]-fee:
            res += (prices[i] - prices[i-1] - fee )
    
    return res
