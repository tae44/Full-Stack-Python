import json

s = '{"name": "jeff", "age": 19}'
li = '[11, 22, 33]'

r1 = json.loads(s)
r2 = json.loads(li)

print(r1, type(r1))
print(r2, type(r2))

ss = {"name": "jeff", "age": 19}
r3 = json.dumps(ss)
print(r3, type(r3))
