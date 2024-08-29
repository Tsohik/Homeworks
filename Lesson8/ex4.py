#Write a Python function that takes two sets as input and returns a new set containing elements that are present in either of the input sets, but not in both.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference = (set1 - set2) | (set2 - set1)
print(symmetric_difference)
