from math import sqrt
import random

def walk(reb, vzr, x1, y1, x2, y2, x, y, tim):
    # 1 и 2
    t = 1
    r = k = 0
    while t <= tim:
        t += 1
        # 3
        object1 = random.randint(1, 2)
        object2 = random.randint(1, 2)
        # пусть 1- движение по горизонтали,
        # 2- по вертикали.
        # Далее в пункте 4 в зависимости от сгенерированного числа нужно
        # обновлять координаты с помощью заявления "if"
        # 4
        if object1 % 2 == 1:
            x1 = x1 + 1
        elif object1 % 2 == 0:
            y1 = y1 + 1

        if object2 % 2 == 1:
            x2 = x2 - 1
        elif object2 % 2 == 0:
            y2 = y2 - 1
        # 5
        if x1 == 301:
            x1 = 1
        elif x1 == -1:
            x1 = 299
        if y1 == 301:
            y1 = 1
        elif y1 == -1:
            y1 = 299
        if x2 == 301:
            x2 = 1
        elif x2 == -1:
            x2 = 299
        if y2 == 301:
            y2 = 1
        elif y2 == -1:
            y2 = 299
        # 6
        c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # 7
        if c <= reb:
            r = r + 1
        if c <= vzr:
            k = k + 1
    return r, k
def fun(wlist, n, p, ts):
    midw = w2 = 0

    for i in range(n):
        # суммарное время "видения"
        midw += wlist[i]

        w2 += wlist[i] ** 2

    # среднее время "видения"
    midw = midw / n

    # оценка стандарта
    sw = sqrt((w2 - n * midw ** 2) / (n - 1))

    # довер. интервал
    pin_w = sw * ts / sqrt(n)

    return midw, pin_w


def main():
    reb = 80
    vzr = 40
    x = 300
    y = 300
    x1 = 1
    x2 = 300
    y1 = 1
    y2 = 300
    tim = 600
    # число экспериментов
    n = 100
    #плюс-минус
    ss = u'\u00B1'
    # довер. интервал
    p = 0.95
    # постоянная Стьюдента
    ts = 1.644854
    rw = []
    kw = []
    for _ in range(n):
        tr, tk = walk(reb, vzr, x1, y1, x2, y2, x, y, tim)
        rw.append(tr)
        kw.append(tk)
    midr, pin_r = fun(rw, n, p, ts)
    print(
        'В среднем ребёнок видит взрослого \n{:.3f} {} {:.3f} секунд\n '.format(midr, ss, pin_r))
    midk, pin_k = fun(kw, n, p, ts)
    print('В среднем взрослый видит ребёнка \n{:.3f} {} {:.3f} секунд '.format(midk, ss, pin_k))


main()