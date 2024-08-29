#Develop a simple dice rolling simulator. Generate random numbers between 1 and 6 to simulate the roll of a six-sided die using the random module.

# import random
# result = random.randint(1, 6)
# print(f"You rolled a {result}.")


import random
def roll_dice():
    result = random.randint(1, 6)
    print(f"You rolled a {result}.")
roll_dice()
