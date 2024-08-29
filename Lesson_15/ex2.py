#Write a python function which will get a number and check is your number great or equal the random number of computer (10-100)if yes print True otherwise False.

import random
def check_number(user_number):
    random_number = random.randint(10, 100)
    if user_number >= random_number:
        print("True")
    else:
        print("False")
user_input = input("Enter a number between 10 and 100: ")
if user_input.isdigit():
    user_number = int(user_input)
    if 10 <= user_number <= 100:
        check_number(user_number)
    else:
        print("The number should be between 10 and 100.")
