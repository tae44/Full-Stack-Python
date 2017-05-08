import re

s = '1 - 2 * ((60 - 30 + (-40 / 5) * (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (16 - 3 * 2))'

def f1(x):
    return 1

while True:
    print(s)
    ret = re.split('\(([^()]+)\)', s, 1)
    if len(ret) == 3:
        before = ret[0]
        middel = ret[1]
        affter = ret[2]
        new = before + str(f1(middel)) + affter
        s = new
    else:
        final = f1(ret)
        print(final)
        break
