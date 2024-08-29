#Write a function in python to read the content from a text file "example.txt" line by line and display the same on screen.

def read_and_display(test):
    with open("test.txt","r") as file:
        for line in file:
            print(line, end='')
read_and_display('test.txt')
