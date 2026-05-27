def best_trade(prices):
    n = len(prices)

    min_price = prices[0]
    min_day = 0

    max_profit = 0
    buy_day = -1
    sell_day = -1

    for i in range(1, n):

        # прибыль если продать сегодня
        profit = prices[i] - min_price

        # нашли лучший вариант
        if profit > max_profit:
            max_profit = profit
            buy_day = min_day
            sell_day = i

        # обновляем минимальную цену
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i

    if max_profit <= 0:
        return "Прибыль получить невозможно"

    return (
        f"Покупать в день {buy_day + 1}, "
        f"продавать в день {sell_day + 1}, "
        f"прибыль = {max_profit}"
    )


# пример
prices = [9, 1, 5]

print(best_trade(prices))