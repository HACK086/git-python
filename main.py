import walk
import fun


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
    # символ плюс-минус
    ss = u'\u00B1'
    # довер. интервал
    p = 0.95
    # постоянная Стьюдента
    ts = 1.644854
    rw = []
    kw = []
    for _ in range(n):
        tr, tk = walk.walk(reb, vzr, x1, y1, x2, y2, x, y, tim)
        rw.append(tr)
        kw.append(tk)
    midr, pin_r = fun.fun(rw, n, p, ts)
    print('В среднем ребёнок видит взрослого \n{:.3f} {} {:.3f} секунд\n '.format(midr, ss, pin_r))
    midk, pin_k = fun.fun(kw, n, p, ts)
    print('В среднем взрослый видит ребёнка \n{:.3f} {} {:.3f} секунд '.format(midk, ss, pin_k))


main()