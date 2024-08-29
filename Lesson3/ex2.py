#Write a Python program to get the largest number from a list.

numbers = [1,2,3,4,6]
largest_number = numbers[0]
for number in numbers[1:]:
    if number > largest_number:
     largest_number = number
print("The largest number in the list is:", largest_number)
