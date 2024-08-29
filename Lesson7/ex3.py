#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
s1 = "programing"
s2 = "pythonprogramming"
set_s1 = set(s1)
set_s2 = set(s2)
balanced = all(char in set_s2 for char in set_s1)
if balanced:
    print("The strings are balanced.")
else:
    print("The strings are not balanced.")
