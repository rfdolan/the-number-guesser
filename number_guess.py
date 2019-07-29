#! /usr/bin/env python

import os
import time
import random 

print("Play the numbers game!")
range = int(input("\nWhat do you want the max number to be?"))

num = random.randrange(range)
print("OK! Thinking of a number between 1 and " + str(range))
thinkingTime = random.randrange(7)
while thinkingTime > 0:
	print(". ", end="", flush=True)
	thinkingTime -= 1
	time.sleep(1)

print("\nI've got it!\n")
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
