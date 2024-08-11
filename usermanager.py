from jsonManager import JsonManager
import hashlib

filename = 'data/users.json'
user_manager = JsonManager(filename)


class UserManager:
    def __init__(self, email):
        self.email = email

    def register_a_user(self, password, full_name, age, gender):
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            data = user_manager.read()
            data.append({
                'gmail': self.email,
                'full_name': full_name,
                'age': age,
                'gender': gender,
                'password': hashed_password,
                'is_active': False
            })
            user_manager.write(data)
            return True
        except Exception as e:
            print(e)
            return False

    def check_email(self):
        try:
            data = user_manager.read()
            for user in data:
                if user['gmail'] == self.email:
                    return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def check_password(self, password):
        try:
            data = user_manager.read()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            for user in data:
                if user['gmail'] == self.email:
                    if user['password'] == hashed_password:
                        return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def show_all_users():
        try:
            data = user_manager.read()
            print('Full name - Email')
            for user in data:
                print(f"{user['full_name']} - {user['gmail']}")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def all_to_false():
        data = user_manager.read()
        for user in data:
            user['is_active'] = False
        user_manager.write(data)
        return True

    def is_active_true(self):
        data = user_manager.read()
        for user in data:
            if user['gmail'] == self.email:
                user['is_active'] = True
                user_manager.write(data)
                return True
