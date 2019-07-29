#! /usr/bin/env python

import time
import random 
import math 

print("Play the numbers game!")
num = int(input("\nWhat number would you like to find? "))
range = int(input("\nWhat do you want the range to be? "))
while range <= num:
	range = int(input("Please enter a valid number for the range. "))

print("\nOk, finding the number.....\n")
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
