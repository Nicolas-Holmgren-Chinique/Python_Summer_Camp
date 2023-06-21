"""This is how my guessing game turned out


How did your guessing game turn out as

"""

import random

print("**** Hello Welcome to my guessing game ****")
print("Guess correctly and you win a prize")



rndm_num = random.randint(1, 10)

chances = 4

while chances > 0:
    user_guess = int(input("Guess a number between 1-10 "))

    if user_guess == rndm_num:
        print("Nice, you guessed the right number! ")

    else:
        print(f"Sorry, that is the wrong number. Try again, you have {chances} left.")
        chances -= 1

if chances == 0:
    print(f"Sorry, you ran out of chances. The correct number was, {rndm_num}")