#! /usr/bin/env python

import os
import time
import random 
import math

print("Play the numbers game!")
range = int(input("\nWhat do you want the max number to be?"))

num = random.randrange(range)
print("OK! Thinking of a number between 1 and " + str(range))
thinkingTime = random.randrange(7)
while thinkingTime > 0:
	print(". ", end="", flush=True)
	thinkingTime -= 1
	time.sleep(1)

guess = ""
optNumGuesses = 0
maxNum = range
minNum = 0
while guess != num:
	guess = math.floor((maxNum + minNum)/2)
	if guess < num:
		minNum = guess
	elif guess > num:
		maxNum = guess

	optNumGuesses += 1	

print("\nI've got it!")
guess = ""
numGuesses = 0
while guess != num:
	guess = int(input("\nGive it your best shot: "))
	if guess < num:
		print("A little low there boss.")
	elif guess > num:
		print("A little high there boss.")

	numGuesses += 1	
print("YOU DID IT!! It only took you " + str(numGuesses) + " guesses!")
print("Binary search finds this number in " + str(optNumGuesses) + " guesses.")
