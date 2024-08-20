import json

user_file = 'user_data.json'

def save_user(username, password):
    user_data = {'username': username, 'password': password}
    with open(user_file, 'a') as file:
        json.dump(user_data, file)
        file.write('\n')

def is_valid_password(password):
    return len(password) >= 8 and password[0].isalpha()

def create_user():
    while True:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")

        if is_valid_password(password):
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                save_user(username, password)
                print("User created successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Invalid password. Please follow the password rules.")

def login_user():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open(user_file) as file:
            for line in file:
                user_data = json.loads(line)
                if user_data['username'] == username and user_data['password'] == password:
                    print("Welcome, {}!".format(username))
                    return

        print("Incorrect username or password. {} attempts remaining.".format(attempts - 1))
        attempts -= 1

    print("Locked out. Too many unsuccessful attempts.")


while True:
    print("\nMenu:")
    print("1. New user")
    print("2. Existing user")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
         print("Exiting the program. Goodbye!")
         break
    else:
         print("Invalid choice. Please enter 1, 2, or 3.")
