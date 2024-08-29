 #Write a function display_words() in python to read text from a text file "example.txt", and display those words, which are less than 4 characters
def display_words():
    with open('test.txt', 'r') as file:
        content = file.read()
        words = content.split()
        for word in words:
            if len(word) < 4:
                print(word)
display_words()
