#Write a Python function to calculate count of each letter in string

input_string = "Hello, World!"
input_string = input_string.lower()
letter_count = {}
for char in input_string:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
print(letter_count)
