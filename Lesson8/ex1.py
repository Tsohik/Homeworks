#Write a Python function that takes two sets as input and returns a new set containing elements that are present in both input sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set()
for element in set1:
    if element in set2:
        result.add(element)
print("Common elements:", result)
