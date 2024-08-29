#Write a function in Python to count and display the total number of words in a text file.

def count_words(test):
    with open("test.txt", 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"count_words:{word_count}")
count_words("test.txt")
