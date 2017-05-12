def a():
    inp = input('请输入模块名: ') # p_json
    ii = __import__(inp)
    inp_func = input('请输入函数名: ') # tp
    f = getattr(ii, inp_func)
    ret = f()
    print(ret)

def b():
    import p_json

    url = input('请输入url: ')
    inp = url.split('/')[-1]
    if hasattr(p_json, inp):
        f = getattr(p_json, inp)
        ret = f()
        print(ret)
    else:
        print('404')

if __name__ == '__main__':
    b()
