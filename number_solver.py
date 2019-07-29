#! /usr/bin/env python

import time
import random 
import math 

print("Play the numbers game!")
range = int(input("\nWhat do you want the max number to be? "))

num = random.randrange(range)
print("OK! Thinking of a number between 0 and " + str(range))
thinkingTime = 2 + random.randrange(4)
while thinkingTime > 0:
	print(". ", end="", flush=True)
	thinkingTime -= 1
	time.sleep(1)

print("\nI've got it!\n")
numGuesses = 0
maxNum = range
minNum = 0
guess = ""
while guess != num:
	guess = math.floor((maxNum + minNum)/2)
	print(str(guess))
	if guess < num:
		minNum = guess
		print("A little low there boss.")
	elif guess > num:
		maxNum = guess
		print("A little high there boss.")

	numGuesses += 1	
print("You got it! It was " + str(num))
print("It took " + str(numGuesses) + " guesses.")
