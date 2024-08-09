from usermanager import UserManager


# admin login = 'admin'
# admin password = 'admin'
def user_menu(email):
    input('User Menu: ')
    pass


def admin_menu():
    input('Admin Menu: ')
    pass


def auth_menu():
    text = """
    1. Register.
    2. Login
    3. Exit
    """
    user_input = input(text)
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
    elif user_input == '3':
        exit()
    else:
        print('Invalid Input. Try again!')
        auth_menu()


if __name__ == '__main__':
    pass
