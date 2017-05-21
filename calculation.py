import re

c = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

#inputs = '1 - 2 * ((60 - 30 + (-40 / 5) * (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (16 - 3 * 2))'
s = '-40 / 5'

def calculation(x):
    ret = re.split('\s+', x)
    print(ret)

calculation(s)
