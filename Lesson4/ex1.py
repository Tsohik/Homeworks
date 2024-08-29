#Write a program that takes a list of numbers as input and counts the number of even numbers in the list. Use a for loop, an if statement, and the modulus operator (%) to determine if a number is even or odd.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(f"Number of even numbers in the list: {even_count}")
