def billboard(x, r):

    n = len(x)

    # p[i] — последний совместимый щит
    p = [-1] * n

    for i in range(n):

        for j in range(i - 1, -1, -1):

            if x[i] - x[j] > 5:
                p[i] = j
                break

    # dp[i] — максимум прибыли до i
    dp = [0] * n

    dp[0] = r[0]

    for i in range(1, n):

        take = r[i]

        if p[i] != -1:
            take += dp[p[i]]

        skip = dp[i - 1]

        dp[i] = max(take, skip)

    # восстановление ответа
    result = []

    i = n - 1

    while i >= 0:

        take = r[i]

        if p[i] != -1:
            take += dp[p[i]]

        skip = dp[i - 1] if i > 0 else 0

        # щит выбран
        if take > skip:

            result.append(x[i])

            i = p[i]

        # щит не выбран
        else:
            i -= 1

    result.reverse()

    return dp[n - 1], result


# пример
x = [6, 7, 12, 14]
r = [5, 6, 5, 1]

profit, coords = billboard(x, r)

print("Максимальная прибыль:", profit)
print("Координаты щитов:", coords)
