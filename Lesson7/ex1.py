#Arrange string characters such that lowercase letters should come first


test = "HAYastan"
lowercase_chars = ""
uppercase_chars = ""
for char in test:
    if char.islower():
        lowercase_chars += char
    if char.isupper():
        uppercase_chars += char
result = lowercase_chars + uppercase_chars
print(result)
