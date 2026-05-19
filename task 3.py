# Create a simple project where the computer thinks of a number between 1 and 100, and the user has to guess it.
import random
n = random.randint(1, 100)
guess = 0
while guess != n :
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
print("Excellent! You guessed the number.")
