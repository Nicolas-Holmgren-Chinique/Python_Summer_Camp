"""
Here is my program, this is similar to rock paper scissors, but instead it is ice, fire, and water

run the code to see what happens.


"""


from random import randint

print("****************************")
print("Welcome to the fire, ice, and water game!")
print("You will play this game against our champion computer Zor")
print("To play, enter 1 for fire, 2 for ice, and 3 for water")
print("Fire wins against ice")
print("Ice wins against water")
print("Water wins against fire")
print("****************************")
print()

playerName = input("What is your name? ")

play = "y"

while play.lower() == "y":
    playerChoice = input("Enter 1 for fire, 2 for ice, 3 for water, or x to exit the program: ")

    if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
        ZorChoice = randint(1, 3)

        if int(playerChoice) == ZorChoice:
            message = "Draw game - no winner!"
        elif int(playerChoice) == 1 and ZorChoice == 2:
            message = "Fire beats ice... Zor wins!"
        elif int(playerChoice) == 1 and ZorChoice == 3:
            message = "Fire beats ice... " + playerName + " wins!"
        elif int(playerChoice) == 2 and ZorChoice == 1:
            message = "Ice beats fire... " + playerName + " wins!"
        elif int(playerChoice) == 2 and ZorChoice == 3:
            message = "Ice beats water... Zor wins!"
        elif int(playerChoice) == 3 and ZorChoice == 1:
            message = "Water beats fire... Zor wins!"
        elif int(playerChoice) == 3 and ZorChoice == 2:
            message = "Water beats ice... " + playerName + " wins!"

        print(message)

    elif playerChoice.lower() == "x":
        print("Goodbye!")
        break

    else:
        print(playerChoice, "is not a valid choice!")
        print("You must enter 1, 2, or 3 to play the game or x to exit")
        print()
