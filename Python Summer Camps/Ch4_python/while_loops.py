"""
While loop excersise

create a variable called age and = it to your age
then make the while loop which should while age less than 18 
print you can't vote 

but the while loop should also have a if statement to check if age is greater than or = to 18

what your results should look like:
age = 12
sorry you can't vote you are to young

age = 18
you can vote 

age = 28
you can vote

Name:

Date:

"""

# If you get stuck ask for help

# age = 19 

# while age < 18:
#     print("sorry you cant vote yet")
#     age += 1
# else:
#     print("you can vote")



# countdown = 10 

# while countdown != 0:
#     print(countdown)
#     countdown -= 1
# else: 
#     print("blast off")

# def movie_app():
#     movie_list = []

#     ask_user = input("Would like to add a movie to the list 'y' for yes, or 'n' for no ")

#     while ask_user.lower() == 'y':
#         add_movie = input("What movie do you want to add ")
#         movie_list.append(add_movie)
#         print(movie_list)

#         another_movie = input("add another movie ")
#         if another_movie.lower != 'y':
#             break

#     else: 
#         print("pick a movie ")

# if "__main__" == __name__:
#     movie_app()












movie_list = []


ask_user = input("Would you like to add a movie to the list 'y' for yes 'n' for no ")

if ask_user.lower() == 'y':
    add_movie = input("What movie do you want to add ")
    movie_list.append(add_movie)
    print(movie_list)
else:
    movie_to_watch = input("pick a movie to watch")




"""

"""

import random


# cards = {"Queen": "hearts", "King": "diamond", "2": "clover", "6": "diamond", "10": "spade",}
# print(cards)
# convert_to_list = list(cards.items())
# random.shuffle(convert_to_list)
# back_to_dictonary = dict(convert_to_list)
# print(back_to_dictonary)


# age = input("Enter your age: ")


def music():
    music_list = []

    user_question = input("would you like to add a song to your list 'y', for yes and 'n' for no ")

    while user_question == 'y':
    
        add_song = input("What song do you want to add ")
        music_list.append(add_song)
        print(f"your playlist is {music_list}")
        ask = input("do you want add another song ")

        if ask.lower() == 'n':
            break
    else:
        # music_select = input("Enter a song ")
        # return music_select
        print("not valid")
    
    shuffle_list = input("would you like to shuffle your playlist 'y' or 'n' ")
 
    if shuffle_list == 'y':
        random.shuffle(music_list)
        print(music_list)
    

if "__main__" == __name__:
    music()




