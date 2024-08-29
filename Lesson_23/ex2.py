#Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

string = "hello world"
frequency = {char: string.count(char) for char in set(string)}
print(frequency)
