#Given a string, create a dictionary where keys are characters, and values are their ASCII values.

input_string = "hello"
ascii_dict = {char: ord(char) for char in input_string}
print(ascii_dict)
