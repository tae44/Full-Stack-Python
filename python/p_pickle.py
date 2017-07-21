import pickle
import json

account_file = 'account.db'
account_json = 'account.json'

def a(x):
    account = {
        1000: {
            'name': 'jeff',
            'password': 123,
            'balance': 10000
        },
        1001: {
                'name': 'jane',
                'password': 123,
                'balance': 10500
            }
    }
    if x == 1:
        f = open(account_file, 'wb')
        # f.write(pickle.dumps(account))
        pickle.dump(account, f)
        f.close()
    else:
        f = open(account_json, 'wb')
        json.dump(account, f)
        f.close()

def b(x):
    id = int(input('消费者ID: '))
    pay = int(input('花费了多少钱: '))
    if x == 1:
        f = open(account_file, 'r+b')
        # account = pickle.loads(f.read())
        account = pickle.load(f)
        account[id]['balance'] -= pay
        f.seek(0)
        # f.write(pickle.dumps(account))
        pickle.dump(account, f)
        f.close()
    else:
        f = open(account_json, 'r+b')
        account = json.load(f)
        account[id]['balance'] -= pay
        f.seek(0)
        json.dump(account, f)
        f.close()

def c(x):
    if x == 1:
        f = open(account_file, 'rb')
        # account = pickle.loads(f.read())
        account = pickle.load(f)
        print(account)
        f.close()
    else:
        f = open(account_file, 'rb')
        account = json.load(f)
        print(account)
        f.close()

if __name__ == '__main__':
    a(2)
