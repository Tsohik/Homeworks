#Create a list of vowels present in a given word.

word = "hello"
vowels = "areko"
lst = [char for char in set(word.lower()) if char in vowels]
print(lst)
