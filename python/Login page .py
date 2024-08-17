# Dictionary of username-password pairs
user_db = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in user_db and user_db[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

# Example usage
login()
