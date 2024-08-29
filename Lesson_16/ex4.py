#Write a simple login system where the user enters a username and password. Handle the KeyError by raising a custom exception if the username is not found in the users database(dictionary).

def login(users, username, password):
    try:
        saved_password = users[username]
        if saved_password == password:
            print("Login successful.")
        else:
            print("Incorrect password.")
    except KeyError:
        print("Error: Username not found.")

users = {
    "simon": "12345",
    "ani": "python1",
}
username = input("Enter your username: ")
password = input("Enter your password: ")
login(users, username, password)
