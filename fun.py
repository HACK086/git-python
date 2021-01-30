def fun(wlist, n, p, ts):
    import math
    midw = w2 = 0

    for i in range(n):
        # суммарное время видимости
        midw += wlist[i]

        w2 += wlist[i] ** 2

    # среднее время видимости
    midw = midw / n

    sw = math.sqrt((w2 - n * midw ** 2) / (n - 1))

    # довер. интервал
    pin_w = sw * ts / math.sqrt(n)

    return midw, pin_w
