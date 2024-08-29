#3. Write a Python program to remove the n-th index character from a nonempty string.

sample_string = 'abcdefgh'
n = 3
result = sample_string[:n] + sample_string[n+1:]
print(result)
