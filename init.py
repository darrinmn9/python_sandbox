def profit(stock_prices):
    if len(stock_prices) < 2:
        return None

    min_price = stock_prices[0]
    profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        min_price = min(min_price, price)
        current_profit = price - min_price
        if (current_profit > profit):
            profit = current_profit

    return profit

print(profit([12, 11, 15, 3, 10]))
print(profit([10, 12, 14, 12, 13, 11, 8, 7, 6, 13, 23, 45, 11, 10]))
print(profit([1]))
