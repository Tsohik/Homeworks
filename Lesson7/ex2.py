#Count all letters, digits, and special symbols from a given string

input_string = "Hello, World! 1234"
letter_count = 0
digit_count = 0
special_count = 0
for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isspace():
        special_count += 1

print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Special symbols: {special_count}")
