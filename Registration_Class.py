from Grocery_Database import Database
from string import ascii_lowercase as low_case
from string import ascii_uppercase as up_case
import random


class Registration:
    names = []
    phone_numbers = []
    email_domains = ("@yahoo.com", "@gmail.com", "@hotmail.com,"
                     "@outlook.com", "@live.co.uk", "@ymail.com",
                     "@yandex.com")

    def get_name(self):
        while True:
            first = input("\nEnter your first name: ")
            if first.isalpha():
                break
            else:
                print("first name should only contain alphabets")

        while True:
            last = input("\nEnter your last name/surname: ")
            if last.isalpha():
                break
            else:
                print("last/surname should only contain alphabets")

        full_name = first + " " + last
        self.names.append(full_name.upper())

    def get_username(self):
        while True:
            username = input("\nEnter your username: ")
            if username in Database.user_name_list:
                print(f"{username} is already taken, Choose another username")
            else:
                if username.isalnum():
                    Database.user_name_list.append(username)
                    break
                else:
                    print(f"Username can only contain alphabets and digits.")
        return username

    def get_email(self):
        while True:
            email = input("\nEnter your email: ")
            if email in Database.emails:
                print(f"{email} is taken")
            else:
                if email[0] in low_case or email[0] in up_case:
                    if email.endswith(self.email_domains):
                        Database.emails.append(email)
                        break
                    else:
                        print("Invalid email")
                else:
                    print("Email can only start with alphabets")

    def get_passsword(self):
        no_of_lower_case = 2
        no_of_upper_case = 3
        no_of_characters = 3
        no_of_digits = 2

        initial_password = []
        # Get uppercase letters
        get_upper_case = [upper for upper in up_case]
        get_lower_case = [lower for lower in low_case]
        get_characters = [chr(character) for character in range(33, 48)]
        get_characters += [chr(character) for character in range(48, 58)]
        get_digit = [chr(digit) for digit in range(58, 65)]

        for ini_password in range(no_of_lower_case):
            initial_password.append(random.choice(get_lower_case))

        for ini_password in range(no_of_upper_case):
            initial_password.append(random.choice(get_upper_case))

        for ini_password in range(no_of_characters):
            initial_password.append(random.choice(get_characters))

        for ini_password in range(no_of_digits):
            initial_password.append(random.choice(get_digit))
        random.shuffle(initial_password)
        password = "".join(initial_password)

        return password

    def get_phone_number(self):
        while True:
            number = input("\nEnter your phone number: ")
            if number in self.phone_numbers:
                print(f"phone number has been used by another customer")
            else:
                self.phone_numbers.append(number)
                break


















