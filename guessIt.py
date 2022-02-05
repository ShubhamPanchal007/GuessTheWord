from words import words
import random


def GuessIt(words):
    randWord = random.choice(words)
    usedGuessedWords_List = []
    lives = 7
    while lives > 0:
        usedGuessedWords_String = "".join(usedGuessedWords_List)
        camofladgedRealWord = [i if i in usedGuessedWords_String else '-' for i in randWord]
        camofladgedRealWord_string = "".join(camofladgedRealWord)
        print("#######################################*******JUST GUESS, NO GAS*******#######################################")
        print(f"{lives} lives left!")
        print(f"Word: {camofladgedRealWord_string.upper()}")
        if(camofladgedRealWord_string == randWord):
                print(f"YOU GUESSED ITT-----> {randWord.upper()}!")
                break

        userGuess = input(f"You have used these: {usedGuessedWords_String.upper()}\nNow Type and Enter to guess a word: ")
        if(userGuess in usedGuessedWords_String):
                print("*******USED WORD DETECTED*******")
        elif(userGuess in randWord):
             usedGuessedWords_List.append(userGuess)
        else:
            usedGuessedWords_List.append(userGuess)
            lives -=1
    if(lives == 0):
            print(F"YOU LOSE, THE WORD WAS {randWord.upper()}")

   

GuessIt(words)
