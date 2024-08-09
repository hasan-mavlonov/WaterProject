from jsonManager import JsonManager
import hashlib

filename = 'data/users.json'


class UserManager:
    def __init__(self, email):
        self.email = email

    def register_a_user(self, password, full_name, age, gender):
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            data = JsonManager(filename).read()
            data.append({
                'gmail': self.email,
                'full_name': full_name,
                'age': age,
                'gender': gender,
                'password': hashed_password
            })
            if JsonManager(filename).write(data):
                return True
        except Exception as e:
            print(e)
            return False

    def check_email(self):
        try:
            data = JsonManager(filename).read()
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
            data = JsonManager(filename).read()
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
            data = JsonManager(filename).read()
            for user in data:
                print(user['gmail'])
            return True
        except Exception as e:
            print(e)
            return False
