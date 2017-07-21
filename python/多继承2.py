'''
        B
A       C
    D
'''

class A:
    def f(self):
        print('A')

class B:
    def s(self):
        print('B')
        self.f()    # self还是D

class C(B):
    def f(self):
        print('C')

class D(A, C):
    pass

obj = D()
obj.s()

# class A:
#     def __init__(self):
#         self.name = 'A'
#         print('A init')
#
# class B(A):
#     def __init__(self):
#         self.age = 18
#         print('B init')
#         # A.__init__(self)
#         super(B, self).__init__()
#
# b = B()
# print(b.__dict__)
