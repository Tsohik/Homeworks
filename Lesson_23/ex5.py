
#Given a list of words, create a dictionary where keys are words, and values are their lengths, but only for words with lengths greater than 3.

words = ["apple", "cat", "dog", "rat", "elephant"]
filtered_lengths = {word: len(word) for word in words if len(word) > 3}
print(filtered_lengths)
