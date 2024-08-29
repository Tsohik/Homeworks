#Write a function that checks the length of a string provided by the user. Handle the TypeError by raising a custom exception if the input is not a string.

def check_string_len(user_input):
    try:
        if type(user_input) is not str:
            raise TypeError("Input must be a string.")
        print(f"The length of the string is: {len(user_input)}")
    except TypeError as e:
        print(e)

user_input = input("Enter a string: ")
check_string_len(user_input)
