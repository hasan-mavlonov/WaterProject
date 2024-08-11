from usermanager import UserManager
from balance import add_balance_order


admin_email = 'admin'
admin_password = 'admin'


def user_menu(email):
    UserManager(email).is_active_true()
    text = """
    1.Add balance water
    2.Show my balance
    3.Buy water from balance
    4.Log-out
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_balance_order()
        return user_menu(email)
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        UserManager(email).all_to_false()
        return auth_menu()
    else:
        print('Wrong number, try again!')
        return user_menu(email)


def admin_menu():
    text = """
        1.Show all users
        2.Show each user's balance
        3.Log-out
        """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        UserManager.show_all_users()
        return admin_menu()
    elif user_input == '2':
        pass
    elif user_input == '3':
        return auth_menu()
    else:
        print('Wrong number, try again!')
        return admin_menu()


def auth_menu():
    UserManager.all_to_false()
    text = """
    1. Register.
    2. Login
    3. Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        email = input("Email: ")
        if email == 'admin':
            password = input('Enter your password: ')
            if password == 'admin':
                admin_menu()
            else:
                print("Wrong password!")
                auth_menu()
        elif not UserManager(email).check_email():
            user = UserManager(email)
            password = input("Password: ")
            full_name = input('Enter your full name: ')
            age = input("Enter your age: ")
            gender = input("Enter your gender: ")
            if user.register_a_user(password, full_name, age, gender):
                print('The user successfully registered.')
                auth_menu()
        else:
            print('The user already exists.')
            auth_menu()
    elif user_input == '2':
        email = input("Email: ")
        if email == 'admin':
            password = input("Enter your password: ")
            if password == 'admin':
                admin_menu()
            else:
                print("Wrong password!")
                auth_menu()
        elif UserManager(email).check_email():
            password = input("Password: ")
            if UserManager(email).check_password(password):
                user_menu(email)
        else:
            print('Wrong email')
            return auth_menu()
    elif user_input == '3':
        exit()
    else:
        print('Invalid Input. Try again!')
        auth_menu()


if __name__ == '__main__':
    auth_menu()
