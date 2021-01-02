import random

n = 20 
num_to_be_guessed = int(n * random.random()) + 1

guess = 0

while guess != num_to_be_guessed:
    guess = int(input("Enter new number:"))
    if guess > 0:
        if num_to_be_guessed < guess:
            print("The number you have guessed is bigger than the original number!")
        elif num_to_be_guessed > guess:
            print("The number you have guessed is smaller than the original number!")
        else:
            print("you have guessed it correctly: ", num_to_be_guessed)
    else:
        print("Enter positive number")