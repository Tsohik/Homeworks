#Write a Python program to square and cube every number in a given list of integers using Lambda.

numbers = [1,2,3,4,5]
square_numbers = list(map(lambda x: x ** 2, numbers))
cube_numbers = list(map(lambda x: x ** 3, numbers))
print(f"Squared numbers: {square_numbers}")
print(f"Cubed numbers: {cube_numbers}")
