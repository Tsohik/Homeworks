#Print the multiplication table of 5 using a for loop and f”strings”. The table should be printed up to 10.

num = 5
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")
