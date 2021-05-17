# Test Version: Edit This so it doesnt ruin Proper H/L Game
import math
import random

# Functions

# Check for amount of rounds and if give value is within correct responses


# Decorates round heading
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Instructions
def instructions():

    print("Welcome to the Higher and Lower Game ")
    print()
    print(
        "Pick how many rounds that you would like to play, pick a number bigger than 0 "
    )
    print("or press <Enter> for continuous mode ")
    print()
    print(
        "For each round, choose a quess that is equal to or between your Highest and Lowest Number "
    )
    print("or xxx to quit")
    print()
    print("You only have a set amount of Guesses")
    print("***** Have Fun! *****")
    print()
    return ""


# Yes / no to see whether yes / no is valid
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Integer Checker
def int_check(question, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        response = input(question).lower()
        exit_code = "xxx"

        if exit_code == "xxx" and response == "xxx":
            return response
        elif exit_code == "xxx" and response == "":
            return response

        situation = ""

        if low is not None and high is not None:
            situation = "both"
        elif low is not None and high is None:
            situation = "low only"

        try:
            response = int(response)

            # checks input is not top high
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between "
                          "{} and {}".format(low, high))
                    continue
            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter an number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("Please enter an integer")
            continue


# main routine

# Game Summary
game_summary = []

# Yes/No List
yes_no_list = ["yes", "no", "xxx"]
# Played Before?
played_before = yes_no("Have you played before? ")
print()

if played_before == "no":
    instructions()

# Set up game parameters (range, number of numbers)
low = int_check("Low number: ")  # uses int input in due course
print()
high = int_check("High number: ", low + 1)  # use int check in due course
print()
rounds = int_check("Rounds: ", 0, exit_code="xxx")
print()
# works out number of guesses
num_range = high - low + 1
max_raw = math.log2(
    num_range)  # finds maximum # of guesses using binear search method
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))
print()

# Rounds
rounds_lost = 0
rounds_won = 0
rounds_played = 0

# Breaks game if Keep_going = no if max rounds are reached
keep_going = "yes"

while keep_going == "yes":

    if keep_going == "no":
        break
    # Rounds Heading:

    # Continuous rounds heading
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

        heading_decoration = "="
        print()
        statement_generator(heading, heading_decoration)
        print()

    # Specific number of rounds heading
    else:
        heading = "Round {} of  {}".format(rounds_played + 1, rounds)

        heading_decoration = "-"
        print()
        statement_generator(heading, heading_decoration)
        print()

    # Spoiler of secret to make testing easier.
    secret = random.randint(low, high)
    print()
    print("Spoiler alert, the secret is", secret)
    print()

    # increase rounds
    rounds_played += 1

    # Round set up (feedback reset, empties old guesses, resets guesses allowed)
    feedback = ""

    guesses_allowed = max_guesses

    already_guessed = []
    guesses_left = guesses_allowed
    num_won = 0

    guess = ""

    # Ask user for guess and give feedback (ie: play game)
    while guess != secret and guesses_left >= 1:

        guess = int_check("Guess: ", low, high, "xxx")
        print()

        if guess == "xxx":
            keep_going = "no"
            print("you asked to quit")
            print()
            break

        else:
            print("You guessed", guess)
            print()

        # checks that guess is not a duplicate
        if guess in already_guessed:
            print("You already guessed that number! Please try again "
                  "You *still* have {} guesses left".format(guesses_left))
            continue

        if rounds_played == rounds:
            keep_going = "no"

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < secret:
                print("Too low, try a higher number. Guesses left: {} ".format(
                    guesses_left))
                print()

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: {} ".format(
                    guesses_left))
                print()
        else:
            if guess < secret:
                print("Too Low!")
                print()
            elif guess > secret:
                print("Too High!")
                print()

        if guess == secret:
            print("Amazing! You got it ")
            print()

        elif guess == secret:
            print("Well done, you got it ")
            print()

        # Failed to guess secret, displays secret
        if guess != secret and guesses_left <= 0:
            print("You have no more guesses left, the secret was", secret)
            feedback = "lost"
            rounds_lost += 1
            print()


    if feedback != "lost":
        feedback = "won"

    rounds_won = rounds_played - rounds_lost

    # Displays Rounds , guesses and whehter game won or lost.
    round_result = "Round {}, guesses: {}, ({}) ".format(
        rounds_played, len(already_guessed), feedback)
    game_summary.append(round_result)

# Game Score
print()
print("**** Game Score ****")
for game in game_summary:
    print(game)

# end of game statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t".format(rounds_won, rounds_lost))
print()

# Notes:
# Add Statement Generator
