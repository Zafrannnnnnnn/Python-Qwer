#!/usr/bin/env python
#Funtion random
import random

def main():
    #start a game 
    """start a genre music guessing game."""
    print("")
    print("Guess the music genre!")
#genre music list
    music=[
        "rock",
        "country",
        "jazz",
        ]
    x = random.choice(music)
    guess = None 

    while x != guess:
#input from user
        guess = str(input("what is the genre music that use electrical insturments im thinking off?:"))
#output yang keluar bedasarkan jawapan pengguna
        if x == guess:
            print("Congratulations {} its the right answer maybe you are just lucky at all".format(guess))
        else:
            print("{} its incorrect answer try again until you get it ".format(guess))
#markah yang ditentukan bedasarkan jawapan 
        score = 0
        if x in guess:
            score=score+1

        print("Your score:" ,score)

            



main()
        



