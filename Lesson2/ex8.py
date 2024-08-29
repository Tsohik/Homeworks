#Input three integers. Output the word “Sorted” if the numbers are listed in a non-increasing or non-decreasing order and “Unsorted” otherwise.
a = 1
b = 3
c = 2
sorted_status = (a <= b <= c) or (a >= b >= c)
print("Sorted" if sorted_status else "Unsorted")
