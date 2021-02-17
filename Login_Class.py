from Grocery_Database import Database
from string import ascii_lowercase as lower_case_alphabets
from string import ascii_uppercase as upper_case_alphabets
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters_list = ["/", "!", "@", "#", "%", "^", "*", ":", ";", "?"]

class Login:
    # Regular user sign in

    def sign_in(self):
        while True:
            username = input("\nEnter your username: ")
            if username in Database.user_name_list:
                break
            else:
                print("Username not found")

        while True:
            password = input("\nEnter your password: ")
            if Database.profile[username] == password:
                return True, username
            else:
                print("Password incorrect")


# If user is logging in for the first time change password
class Password(Login):
    def upper(self, password):
        for letter in upper_case_alphabets:
            if letter in password:
                return True

    def lower(self, password):
        for letter in lower_case_alphabets:
            if letter in password:
                return True

    def characters(self, password):
        for char in characters_list:
            if char in password:
                return True

    def numbers(self, password):
        for number in numbers_list:
            if number in password:
                return True

    def reset_password(self):
        while True:
            password = input("Enter new password: ")
            is_upper = self.upper(password)
            is_lower = self.lower(password)
            is_character = self.characters(password)
            is_number = self.numbers(password)

            if len(password) >= 8:
                if is_upper and is_lower and is_character and is_number:
                    break
                else:
                    print("Password not valid")
            else:
                print("Password should contain at least 8 characters ")

        while True:
            confirm_password = input("Confirm Password: ")
            if confirm_password == password:
                return True
            else:
                print("Password do not match")
                return False


