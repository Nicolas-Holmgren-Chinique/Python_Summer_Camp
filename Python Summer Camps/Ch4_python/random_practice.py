"""
We are going to practice using the random function.

first import random at the top and then 

create a variable and 
follow the steps in the slides

Name: 

Date:

"""

import random 

# user_input = int(input("Enter a number: "))
# guess = random.randint(0, 20)

# chances = 0

# while user_input != guess:
#     print(f"Thats the wrong number, you have {chances} left")
#     chances -= 1 



deck_of_cards = [{"hearts": "queen", "dimonds": "5", "clover": "7"}]
print(deck_of_cards)


random.shuffle(deck_of_cards)

print(deck_of_cards)

new_list = ["hello", "goodbye", 1, 2, 4]

random.shuffle(new_list)
print(new_list)