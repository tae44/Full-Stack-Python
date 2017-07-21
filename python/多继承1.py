'''
    s
a       b
c       d
    e
    
e -> c -> a -> d -> b -> s
'''

class s:
    def f(self):
        print('inputs')

class a(s):
    def f(self):
        print('a')

class b(s):
    def f(self):
        print('b')

class c(a):
    def f(self):
        print('c')

class d(b):
    def f(self):
        print('d')

class e(c, d):
    def f(self):
        print('e')

obj = e()
obj.f()
