import random

def compare_numbers(number, user_guess):
    # Initialize counts for cows and bulls
    cow_count = 0
    bull_count = 0

    # Compare each digit in the number and user_guess
    for i in range(4):
        if user_guess[i] == number[i]:
            bull_count += 1
        elif user_guess[i] in number:
            cow_count += 1

    # Return counts of cows and bulls
    return cow_count, bull_count

playing = True
number = str(random.randint(0, 9999))
guesses = 0
print("Let's play a game of Cowbull!")
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess: ")

    if user_guess.lower() == "exit":
        break

    if len(user_guess) != 4 or not user_guess.isdigit():
        print("Please enter a 4-digit number.")
        continue

    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1

    print("You have {} cows and {} bulls.".format(cowbullcount[0], cowbullcount[1]))

    if cowbullcount[1] == 4:
        playing = False
        print("You win the game after {} guesses! The number was {}".format(guesses, number))
    else:
        print("Your guess isn't quite right, try again.")
