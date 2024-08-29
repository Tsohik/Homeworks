#Given a list of numbers, write a function to find the sum of all numbers in the list that can be divided by 7.

def sum_divisible_by_7(numbers):
    total_sum = 0
    for num in numbers:
        if num % 7 == 0:
            total_sum += num

    return total_sum

numbers = [14, 21, 22, 28, 35, 40, 49]
result = sum_divisible_by_7(numbers)
print(f"The sum of numbers divisible by 7 is: {result}")
