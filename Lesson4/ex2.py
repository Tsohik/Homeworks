#Write a program that takes a string as input and counts the number of vowels (a,
e, i, o, u) in the string. Use a for loop, an if statement, and the in operator to check if a character is a vowel.

input_string = input("")
vowels = 'aeiou'
vowel_count = 0
for char in input_string:
    if char.lower() in vowels:
        vowel_count += 1
print(f"Number of vowels: {vowel_count}")
