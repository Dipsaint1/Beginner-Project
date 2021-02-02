import random

users = {"username": "dipsaint"}
email_list = ["ayodejioladapo15@gmail.com"]
username_list = ["dipsaint"]
profile = {"username": "1234", "password": "1234"}
email_domains = ('@yahoo.com', "@gmail.com", "hotmail.com", "@ymail.com", "@live.net"
                 "outlook.co.uk", "outlook.com", "@yandex.com", "@yahoo.co.uk")
def get_name():           # Get full name
    while True:
        first_name = input(f"First name: ")
        last_name = input(f"Surname/Last name: ")
        middle_name = input(f"Middle name: ")
        first_name, middle_name, last_name = first_name.title(), middle_name.title(), last_name.title()

        if first_name.isalpha() and middle_name.isalpha() and last_name.isalpha():
            profile['first name'], profile[middle_name], profile["last_name"] = first_name, middle_name, last_name
            full_name = (first_name + " " + last_name).title()
            profile["full_name"] = full_name
            break
        else:
            print("invalid input, name should contain only alphabets.")
        print()


def get_username():      #   Create username
    while True:
        username = input("Username: ")
        if username in username_list:
            print(f"{username} exists!")
        else:
            if username.isalpha() or username.isalnum():
                username_list.append(username)      # Add to list of username
                profile["username"] = username      # Add to user profile
                break
            else:
                print("invalid input!, username should contain only alphabets and numbers only")
        print()


def get_email():        # create email
    while True:
        email = input(f"Email: ")
        if email in email_list:
            print(f"{email} exists! ")
        else:   # It's not registered
            if email.endswith((email_domains)):     # Check if the domain is correct
                email_list.append(email)            # Add to email list
                profile["email"] = email            # Add to profile
                break
            else:
                print("invalid email! ")
        print()

def create_password():
    num_lower_case = 3
    num_upper_case = 5
    num_digits = 3
    num_character = 4

    # Get characters from ASCII Table
    get_lower_case = [chr(i) for i in range(97, 123)]
    get_upper_case = [chr(i) for i in range(63, 91)]
    get_digit = [chr(i) for i in range(48, 58)]
    get_character = [chr(i) for i in range(33, 48)]
    get_character += [chr(i) for i in range(58, 65)]

    # Generate characters
    generate_lower_case = []
    for i in range(num_lower_case):
        generate_lower_case.append(random.choice(get_lower_case))

    generate_upper_case = []
    for i in range(num_upper_case):
        generate_upper_case.append(random.choice(get_upper_case))

    generate_digit = []
    for i in range(num_digits):
        generate_digit.append(random.choice(get_digit))

    generate_character = []
    for i in range(num_character):
        generate_character.append(random.choice(get_character))


    # Combine the generated passwords
    temporary_passwords = generate_upper_case + generate_lower_case + generate_digit + generate_character

    random.shuffle(temporary_passwords)
    password = temporary_passwords
    password = "".join(password)
    print(f"Your password is: {password}, please keep it safe.")
    profile['password'] = password

def registration_page():
    get_name()
    get_username()
    get_email()
    create_password()
    print("\nProcessing. Processing.. Processing...")
    print("Registration Successful.")

def login_page():
    while True:
        username = input("\nEnter your username: ")
        if username in username_list:
            break
        else:
            print(f"username not found!")


    # Enter your email:
    while True:
        email = input(f"\nEnter your email: ")
        if email in email_list:
            break
        else:
            print(f"email not registered!")

    # Enter password

    while True:
        password = input(f"enter your password: ")
        if password == profile["password"]:
            break
        else:
            print("Incorrect password")

    print("\nProcessing. Processing.. Processing...")
    print("Login Successful.")

def main():
    print("Welcome to www.cyber9ja.com")
    while True:
        choice = input("Press '1' to sign up or '2' to login: ")
        if choice == '1':       # Signup
            registration_page()
            break
        elif choice == '2':
            login_page()
            break
        else:
            print(f"invalid input! Press '1' to signup or '2' to login")

main()
