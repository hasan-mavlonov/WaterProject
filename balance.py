from jsonManager import JsonManager
from random import randint
from usermanager import filename


file_balance = 'data/balance.json'
balance_manager = JsonManager(file_balance)
user_manager = JsonManager(filename)


def active_user():
    all_users = user_manager.read()
    for user in all_users:
        if user['is_active'] is True:
            return user


class Balance:
    def __init__(self, quantity, price, name, email):
        self.quantity = quantity
        self.price = price
        self.id_num = randint(0, 1_000_000)
        self.name = name
        self.email = email


def add_balance_order():
    print("""
    1. 0-10 -> 1500
    2. 11-25 -> 1400
    3. 26-50 -> 1200
    4. 51-inf -> 1100
    """)
    try:
        quantity = int(input('Enter quantity: '))
        active = active_user()
        if quantity < 10:
            price = 1500
        elif quantity < 25:
            price = 1400
        elif quantity < 50:
            price = 1200
        else:
            price = 1100

        new_balance = Balance(quantity, price, active['full_name'], active['gmail'])
        balance_manager.add(new_balance.__dict__)
        print('Added successfully!')
        return True
    except ValueError:
        print('Quantity must be a whole number!')
        return False


def each_balance():
    all_data = balance_manager.read()
    print('User email - quantity - price')
    for i in all_data:
        print(f"{i['email']} - {i['quantity']} - {i['price']}")


def my_balance():
    all_data = balance_manager.read()
    user = active_user()
    print('User email - quantity - price')
    for i in all_data:
        if i['email'] == user['gmail']:
            print(f"{i['email']} - {i['quantity']} - {i['price']}")
            break
    return


def return_balance():
    all_data = balance_manager.read()
    user = active_user()
    for i in all_data:
        if i['email'] == user['gmail']:
            return i


def buy_water():
    try:
        active = active_user()
        all_data = balance_manager.read()
        quantity = int(input('Enter water quantity: '))
        my_ball = return_balance()
        if quantity <= my_ball['quantity']:
            print('Success!')
            print(f'Total cost: {my_ball["price"]*quantity}')
            print(f'Your balance: {my_ball["quantity"] - quantity}')
            i = 0
            while i < len(all_data):
                if all_data[i]['email'] == active['gmail']:
                    all_data[i]['quantity'] -= quantity
                    balance_manager.write(all_data)
                    return
                i += 1
        else:
            print('You do not have that many products!')
            return
    except ValueError:
        print('Quantity must be a whole number!')
        return buy_water()
