def walk(reb, vzr, x1, y1, x2, y2, x, y, tim):
    import math
    import random
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
        c = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # 7
        if c <= reb:
            r = r + 1
        if c <= vzr:
            k = k + 1
    return [r, k]