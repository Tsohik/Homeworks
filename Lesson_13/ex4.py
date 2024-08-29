#Write a Python program to find intersection of two given arrays using Lambda.

arrays1 = [1, 2, 3, 4, 5]
arrays2 = [4, 5, 6, 7, 8]
intersection = list(filter(lambda x: x in arrays2, arrays1))
print(intersection)
