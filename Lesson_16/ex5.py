#Write a function that prompts the user to enter a number and tries to convert it to an integer. Handle the TypeError exception by printing a message indicating that the input is not a valid number. Use a finally block to print "Type conversion process completed."


try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"The entered number is: {number}")
except ValueError:
    print("Error: The input is not a valid number.")
finally:
    print("Process completed.")
