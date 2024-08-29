#Write a Python program to remove duplicates from a list.

numbers = [1, 2, 3, 4, 5, 3,5]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
     unique_numbers.append(number)
print("The list with duplicates removed:", unique_numbers)
