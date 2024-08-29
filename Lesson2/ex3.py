# Input a two-digit natural number and output the sum of its digits. You can assume that the input will be a two-digit number and need not check that programmatically.


N = 24
tens_digit = N // 10
units_digit = N % 10
sum_of_digits = tens_digit + units_digit
print("The sum of the digits of", N, "is:", sum_of_digits)
