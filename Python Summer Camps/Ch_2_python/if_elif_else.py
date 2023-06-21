"""
Lets practice some if, elif, and else

1. make a variable called grade assgin it to get input from the user, you want them to enter a grade

below is a starter to get you started
grade = inp...

2. make mulitple if elif to check the user input (grade), so first you want to check if the grade is between 90 and 100 which would be an A, 

you want to do the same for the other grades B, C, D, F

Name:

Date:

remeber if you get stuck go back to the slides, ask the coach for help
"""

# Write your code below this line, check the example below if needed




# Here is an example of a similar program to get you started
# Before you test your code out delete the code before so it doesn't mess with your code

age = int(input("What is your age: "))

# note that below we use and, when we use and 
# we are seeing if age is less than 65 and age is greater than equal to 25 
# what that does is check if the users age is between that range.
# With and they both have to be true, age has to be <= 65 and age has to be >= 25

if age > 65:
    print("It's time to retire")

elif age >= 25 and age <= 65:
    print("you must be working")

elif age >= 18 and age <= 24:
    print("You must be in college")

elif age >= 14 and age <= 18:
    print("You must be in high school")
else:
    print("You are a kid and probably in elementry or middle school")
