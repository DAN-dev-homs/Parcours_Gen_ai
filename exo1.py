import random
from config import *

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
# Total allowed chances
ch =7 
# Guess counter
gc = 0                         

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))
 if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break