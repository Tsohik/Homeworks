#Write a Python function to find the Max of three numbers.

a = 10
b = 20
c = 30
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"{max_of_three(a, b, c)}")
