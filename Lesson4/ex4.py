#Write a program that prompts the user to enter a word and checks if it is a palindrome. A palindrome is a word that reads the same backward as forward. Use string slicing and an if-else statement to compare the original word with its reverse.

word = input("Enter a word: ")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")
