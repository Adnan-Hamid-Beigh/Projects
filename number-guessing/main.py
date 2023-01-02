import random
from art import logo
print(logo)
number_of_tries = 0
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(f"Pssst, the correct answer is {number}") Testing
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice == "easy":
  number_of_tries += 10
elif choice == "hard":
  number_of_tries += 5
number_of_tries_left = number_of_tries
print(f"{number_of_tries_left} tries left.")
running = True
while number_of_tries_left <= number_of_tries and number_of_tries_left != 0 and running:
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {guess}")
    running = False
  elif guess < number:
    number_of_tries_left -= 1
    print("Too low. \nGuess Again.")
    print(f"{number_of_tries_left} tries left.")
    
  elif guess > number:
    number_of_tries_left -= 1
    print("Too high. \nGuess Again.")
    print(f"{number_of_tries_left} tries left.")
  if number_of_tries_left == 0:
    print("You've run out of guesses, you lose.")
  