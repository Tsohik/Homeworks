# Write a Python program to check whether a given string is number or not using Lambda.

is_number = lambda s: s.isdigit()
test_string = "1234"
result = is_number(test_string)
print(result)

is_number = lambda s: s.isdigit()
test_string = "1a23b"
result = is_number(test_string)
print(result)
