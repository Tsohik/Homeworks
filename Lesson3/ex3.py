#Write a Python program to get the smallest number from a list.

numbers = [5, 7, 3, 9, 11]
smallest_number = numbers[0]
for number in numbers[1:]:
    if number < smallest_number:
     smallest_number = number
print("The smallest number in the list is:", smallest_number)
