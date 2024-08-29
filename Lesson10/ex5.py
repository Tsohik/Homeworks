#Write a Python program that calculates the Fibonacci sequence up to a given number n
using a while loop. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones.

n = int(input("Enter the maximum number for Fibonacci sequence: "))
a, b = 0, 1
fibonacci_sequence = []
while a <= n:
    fibonacci_sequence.append(a)
    a, b = b, a + b
print("Fibonacci sequence up to", n, ":", fibonacci_sequence)
