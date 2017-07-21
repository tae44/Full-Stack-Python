inp = input('请输入内容: ')
try:
    n = int(inp)
    print(n)
except ValueError as e:
    print(e)
    print('数据类型输入错误')
except IndexError as e:
    print(e)
    print('索引错误')
except Exception as e:
    print(e)
else:
    print('没毛病!')
finally:
    print('无论如何都执行')

# assert 1 == 2

# try:
#     raise ValueError('hello')
# except ValueError as e:
#     print(e)
