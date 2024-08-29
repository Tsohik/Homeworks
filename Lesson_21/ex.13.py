#Write a function that checks if two sets are disjoint (have no common elements).


def are_disjoint(set1, set2):
    intersection = set1 & set2
    return len(intersection) == 0

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 7, 8}

print(f"Set1 and Set2 are disjoint: {are_disjoint(set1, set2)}")
print(f"Set1 and Set3 are disjoint: {are_disjoint(set1, set3)}")
