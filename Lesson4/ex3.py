#Write a program that takes a list of words and a target word as input. The program should find and print all words in the list that contain the target word. Use a for loop, the in operator, and an if statement to check if the target word is present in each word in the list.

word_list = ["Ani","Armen","Vika","Anush","Gor"]
target_word = "Anush"
for word in word_list:
 if target_word in word:
  print(word)
