#Write a python program to add text to a file and display the text in python.txt.

with open("test.txt","a") as file:
    file.write("He doesn't like dogs.")
    file.write("Hello Simon.")
with open("test.txt", "r") as file:
    result = file.read()
    print(result)
