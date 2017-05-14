class Foo:

    static_s = 'good'

    @staticmethod
    def static_f():
        print('i am a static method in Foo')

    @classmethod
    def class_f(cls):
        print('i am a class method in Foo')

    def __init__(self, name):
        print('__init__')
        self.name = name

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)

    def __iter__(self):
        yield 1
        yield 2
        yield 3

    def f(self):
        print('i am a method in Foo')

    @property
    def end(self):
        print('getter')
        print('i am {} in Foo'.format(self.name))

    @end.setter
    def end(self, value):
        print('setter')
        self.name = value


obj = Foo('jeff')
obj()
obj.age = 18

obj['k1']
obj['k1'] = 'v1'
del obj['k1']

r1 = hasattr(Foo, 'name')
r2 = hasattr(Foo, 'f')
r3 = hasattr(Foo, 'age')
r4 = hasattr(Foo, 'static_s')
r5 = hasattr(obj, 'name')
r6 = hasattr(obj, 'f')
r7 = hasattr(obj, 'age')
r8 = hasattr(obj, 'static_s')

print(r1, r2, r3, r4, r5, r6, r7, r8)

Foo.f(obj) # 不推荐
obj.f()

Foo.static_f()
obj.static_f() # 不推荐

obj.class_f() # 不推荐
Foo.class_f()

obj.end
obj.end = 'jane'
obj.end

for i in obj:
    print(i)
