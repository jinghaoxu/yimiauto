import datetime
import time


# 当前时间 ： 2018-01-22 16:26:00.809788
def now():
    return datetime.datetime.now()


# 时间戳：1516609823
def stamp():
    return str(int(time.time()))


if __name__ == '__main__':
    print(1)
