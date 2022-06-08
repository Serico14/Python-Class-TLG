#!/usr/bin/env python3

#Define random number generator
import random

#Character count randomizer
char= int(random.randint(1,7))

#Round count starter
turn= 0

#Character Answer and Question
char_ans= {1:"Frodo", 2:"Sam", 3:"Gandalf", 4:"Aragorn", 5:"Legolas", 6:"Gimli", 7:"Boromir"}
char_question= {1:"Ring Bearer hailing from Shire Town, Who am I?", 2:"Voted Best Wingman in All of Middle Earth, Who am I?", 3:"Known for ingesting more than just tobacco in iconic pipe, Who am I?", 4:"Dunedain roleplaying as Ranger, Who am I?", 5:"Once used a person as skateboard while firing at the same time, Who am I?", 6:"Wife has just as long of a beard as him?", 7:"Took an arrow...or 5 to the chest for being a party foul?"
            } 
#Intro and Question
print("Welcome to Guess that LOTR Character!!!\n3 Guesses & First Name ONLY")

while turn < 3:
    
    guess= input(char_question[char] + "\n")
    
    if not guess.isdigit():
        guess= str(guess)
       
    else:
        print("Please no numbers.Please try again.")
        continue

    turn += 1
    
    if guess == char_ans[char]:
        print("You are correct! It's " + char_ans[char] + ", Middle Earth is saved!")
        break
    elif turn == 3:
        print("You have attempted too many times!\nSauron rules now. GG.")
        break
    else:
        print("Incorrect guess. Try again!")
        
    

