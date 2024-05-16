import easygui
import random

answer = random.randint(1, 100)
tries = 0
number_found = False

while not number_found:
    guess = easygui.integerbox("guess a number between 1 and 100", title="random number game",
                               lowerbound=1, upperbound=100)
    if guess < answer:
        easygui.msgbox("Your number is too low", title="random number game", ok_button="guess again")
        tries += 1
    elif guess > answer:
        easygui.msgbox("Your number is too high", title="random number game", ok_button="guess again")
        tries += 1
    else:
        number_found = True

easygui.msgbox("You got the number in " + str(tries) + " tries.", title="end screen")
