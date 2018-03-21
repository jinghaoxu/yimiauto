def c2(x5):
    if x5 == 3:
        return 1
    elif x5 == 4:
        return 2
    elif x5 == 1:
        return 3
    elif x5 == 2:
        return 4
    else:
        return 0


def c3(x2, x3, x4, x6):
    if x2 == x3 == x4 != x6:
        return 2
    elif x2 == x3 == x6 != x4:
        return 4
    elif x2 == x6 == x4 != x3:
        return 1
    elif x6 == x3 == x4 != x2:
        return 3
    else:
        return 0


def c4(x1, x2, x5, x6, x7, x9, x10):
    if x1 == x5 and x2 != x7 and x1 != x9 and x6 != x10:
        return 1
    elif x1 != x5 and x2 == x7 and x1 != x9 and x6 != x10:
        return 2
    elif x1 != x5 and x2 != x7 and x1 == x9 and x6 != x10:
        return 3
    elif x1 != x5 and x2 != x7 and x1 != x9 and x6 == x10:
        return 4
    else:
        return 0


def c5(x4, x5, x7, x8, x9):
    if x8 == x5 and x4 != x5 and x9 != x5 and x7 != x5:
        return 1
    elif x8 != x5 and x4 == x5 and x9 != x5 and x7 != x5:
        return 2
    elif x8 != x5 and x4 != x5 and x9 == x5 and x7 != x5:
        return 3
    elif x8 != x5 and x4 != x5 and x9 != x5 and x7 == x5:
        return 4
    else:
        return 0


def c6(x1, x2, x3, x4, x5, x6, x8, x9, x10):
    if x2 == x4 == x8 and (x1 != x8 or x6 != x8) and (x3 != x8 or x10 != x8) and (x5 != x8 or x9 != x8):
        return 1
    elif x1 == x6 == x8 and (x2 != x8 or x4 != x8) and (x3 != x8 or x10 != x8) and (x5 != x8 or x9 != x8):
        return 2
    elif x3 == x10 == x8 and (x1 != x8 or x6 != x8) and (x2 != x8 or x4 != x8) and (x5 != x8 or x9 != x8):
        return 3
    elif x5 == x9 == x8 and (x1 != x8 or x6 != x8) and (x3 != x8 or x10 != x8) and (x2 != x8 or x4 != x8):
        return 4
    else:
        return 0


def c7(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    listt = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    a1 = listt.count(1)
    a2 = listt.count(2)
    a3 = listt.count(3)
    a4 = listt.count(4)
    minsum = min(a1, a2, a3, a4)
    if minsum == a3 and minsum != a2 and minsum != a1 and minsum != a4:
        return 1
    elif minsum != a3 and minsum == a2 and minsum != a1 and minsum != a4:
        return 2
    elif minsum != a3 and minsum != a2 and minsum == a1 and minsum != a4:
        return 3
    elif minsum != a3 and minsum != a2 and minsum != a1 and minsum == a4:
        return 4
    else:
        return 0


def c8(x1, x2, x5, x7, x10):
    if abs(x7-x1) != 1 and abs(x5-x1) == 1 and abs(x2-x1) == 1 and abs(x10-x1) == 1:
        return 1
    elif abs(x7-x1) == 1 and abs(x5-x1) != 1 and abs(x2-x1) == 1 and abs(x10-x1) == 1:
        return 2
    elif abs(x7-x1) == 1 and abs(x5-x1) == 1 and abs(x2-x1) != 1 and abs(x10-x1) == 1:
        return 3
    elif abs(x7-x1) == 1 and abs(x5-x1) == 1 and abs(x2-x1) == 1 and abs(x10-x1) != 1:
        return 4
    else:
        return 0


def c9(x1, x2, x5, x6, x9, x10):
    if x1 == x6:
        if x5 != x6 and x5 == x10 and x5 == x2 and x5 == x9:
            return 1
        elif x5 == x6 and x5 != x10 and x5 == x2 and x5 == x9:
            return 2
        elif x5 == x6 and x5 == x10 and x5 != x2 and x5 == x9:
            return 3
        elif x5 == x6 and x5 == x10 and x5 == x2 and x5 != x9:
            return 4
        else:
            return 0
    else:
        if x5 == x6 and x5 != x10 and x5 != x2 and x5 != x9:
            return 1
        elif x5 != x6 and x5 == x10 and x5 != x2 and x5 != x9:
            return 2
        elif x5 != x6 and x5 != x10 and x5 == x2 and x5 != x9:
            return 3
        elif x5 != x6 and x5 != x10 and x5 != x2 and x5 == x9:
            return 4
        else:
            return 0


def c10(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    listt = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    a1 = listt.count(1)
    a2 = listt.count(2)
    a3 = listt.count(3)
    a4 = listt.count(4)
    minsum = min(a1, a2, a3, a4)
    maxsum = max(a1,a2,a3,a4)
    sub = maxsum - minsum
    if sub == 3:
        return 1
    elif sub == 2:
        return 2
    elif sub == 4:
        return 3
    elif sub == 1:
        return 4
    else:
        return 0


for i1 in [1, 2, 3, 4]:
    for i2 in [1, 2, 3, 4]:
        for i3 in [1, 2, 3, 4]:
            for i4 in [1, 2, 3, 4]:
                for i5 in [1, 2, 3, 4]:
                    for i6 in [1, 2, 3, 4]:
                        for i7 in [1, 2, 3, 4]:
                            for i8 in [1, 2, 3, 4]:
                                for i9 in [1, 2, 3, 4]:
                                    for i10 in [1, 2, 3, 4]:
                                        lis1 = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
                                        listtt = [2, 3, 1, 3, 1, 3, 4, 1, 2, 1]

                                        if i2 != c2(i5):  # 判定第2题
                                            continue

                                        if i3 != c3(i2, i3, i4, i6):  # 判定第3题
                                            continue

                                        if i4 != c4(i1, i2, i5, i6, i7, i9, i10):  # 判定第4题
                                            continue

                                        if i5 != c5(i4, i5, i7, i8, i9):  # 判定第5题
                                            continue

                                        if i6 != c6(i1, i2, i3, i4, i5, i6, i8, i9, i10):  # 判定第6题
                                            continue

                                        if i7 != c7(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10):  # 判定第7题
                                            continue

                                        if i8 != c8(i1, i2, i5, i7, i10):  # 判定第8题
                                            continue

                                        if i9 != c9(i1, i2, i5, i6, i9, i10):  # 判定第9题
                                            continue

                                        if i10 != c10(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10):  # 判定第10题
                                            continue
                                        print(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10)