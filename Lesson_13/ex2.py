#Write a Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda s, char: s.startswith(char)
test_string = "Barev"
char = "B"
result = starts_with(test_string, char)
print(result)
