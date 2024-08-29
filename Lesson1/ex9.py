# Append new string in the middle of a given (even number of characters) string Example:

homework9="Armen"
new="lol"
middle_index = len(homework9) // 2
first = homework9[:middle_index]
last = homework9[middle_index:]
result = first + new + last
print(result)
