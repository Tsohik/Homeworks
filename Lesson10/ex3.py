#Write a Python program that calculates the sum of all even numbers between 1 and 100 using a while loop.

num = 2
sum_even = 0
while num <= 100:
    sum_even += num
    num += 2
print(f"The sum of all even numbers between 1 and 100 is: {sum_even}")
