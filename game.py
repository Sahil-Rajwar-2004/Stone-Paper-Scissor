#Stone, Paper and Scissor Game
#This game made by sahil

import random
import time

player = input("Enter your Name:: ")
time.sleep(1)

def main( ):
    com = input("Are you ready to play(y/n): ")
    if com.lower( ) == "y":
        time.sleep(1)
        print("Good Luck",player,"...")
    elif com.lower( ) == "n":
        time.sleep(1)
        print("OK...")
        exit( )
    else:
        print("You Have to give answer in (y/n) please. Try Again... :( ")
        main( )
main( )

time.sleep(2)
print("Loading...")
time.sleep(2)

def main( ):

    list = ["rock","paper","scissor"]
    view = random.choice(list)

    command = input("Choose your object(rock/paper/scissor) or type 'e' to exit!:: ")
    if command.lower( ) == "rock":
        print(view)
        if view == "rock":
            time.sleep(1)
            print("Nice Try",player,"Match Tie!")
            time.sleep(1)
            print("rock = rock")
        elif view == "scissor":
            time.sleep(1)
            print("Nice Match",player,"...You Win!")
            time.sleep(1)
            print("rock > scissor")
        elif view == "paper":
            time.sleep(1)
            print("Better Luck Next",player,"You Lose")
            time.sleep(1)
            print("rock < paper")
        else:
            time.sleep(1)
            print("ERROR :(")
        main( )
    elif command.lower( ) == "paper":
        print(view)
        if view == "rock":
            time.sleep(1)
            print("Nice Match",player,"...You Win!")
            time.sleep(1)
            print("paper > rock")
        elif view == "scissor":
            time.sleep(1)
            print("Better Luck next time",player,"You Loose!")
            time.sleep(1)
            print("paper < scissor")
        elif view == "paper":
            time.sleep(1)
            print("Nice Try",player,"... Match Tie!")
            time.sleep(1)
            print("paper = paper")
        else:
            time.sleep(1)
            print("ERROR :(")
        main( )

    elif command.lower( ) == "scissor":
        print(view)
        if view == "rock":
            time.sleep(1)
            print("Better luck next time",player,"You Loose!")
            time.sleep(1)
            print("scissor < rock")
        elif view == "scissor":
            time.sleep(1)
            print("Nice try",player,"... Match Tie!")
            time.sleep(1)
            print("scissor = scissor")
        elif view == "paper":
            time.sleep(1)
            print("Nice Match",player,"...You Win!")
            time.sleep(1)
            print("scissor > paper")
        else:
            time.sleep(1)
            print("ERROR :(")
        main( )
    elif command.lower( ) == "e":
        ask = input("are you sure(y/n)")
        if ask.lower( ) == "y":
            time.sleep(1)
            print("Hope You Enjoy This game :)")
            time.sleep(1)
            exit( )
        elif ask.lower( ) == "n":
            time.sleep(1)
            print("OK...")
            main( )
        else:
            time.sleep(1)
            print("Please answer in (y/n) try again")
            main( )
    else:
        print("!!Choose the correct object!!")
        main( )
main( )
