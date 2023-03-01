import random

guess_range = 0
answer = 0

while(guess_range <= 10):
    guess_range = int(input("Welcome to the Guessing Game! Up to what number would you like to guess? (hint: pick a number greater than 10): "))
    if guess_range <= 10:
        print("That's too easy! Pick a number greater than 10.")
        continue
    elif guess_range > 10:
        answer = random.randint(1, guess_range)

print("I have chosen a number between 1 and {}. You have 10 chances to guess it.".format(guess_range))

guesses = 0

for i in range(10):

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:

        print("That's not a valid number. Please try again.")
        continue
    
    guesses += 1
    
    if guess == answer:
        print(f"Congratulations! You guessed it right!")
        break
    elif guess < answer:
        print("Too low. Try again.")
    elif guess > answer:
        print("Too high. Try again.")

if guesses == 10 and guess != answer:
    print("You failed to guess correctly. The correct answer was {}.".format(answer))
else:
    print("You used {} guesses. The correct answer was {}.".format(guesses, answer))