#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


def factorial(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x
num = 5
print(factorial(num))
