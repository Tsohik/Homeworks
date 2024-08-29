#Write a Python program to find the second smallest number in a list.

numbers = [1,2,3,4]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    second_smallest = unique_numbers[1]
    print("The second smallest number is:", second_smallest)
