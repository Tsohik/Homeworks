#Write a Python program that asks the user to enter a password. Keep asking for the password until the correct password "secret" is entered. Provide appropriate feedback to the user.

correct_password = "secret"
while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access.")
        break
    else:
        print("Incorrect password, please try again.")
