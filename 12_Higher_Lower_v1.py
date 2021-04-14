
import math
# Functions 

def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

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
                      
for item in range (0,4):        # loop component for easy testing...

    low = int(input("Low: "))   # use int check in due course
    high = int(input("High: ")) # use int check in due course

    range = high - low + 1
    max_raw = math.log2(range) # finds maximum # of guesses using binear search method 
    max_upped = math.ceil(max_raw) # rounds up (ceil --> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))



    secret = range
    guesses_allowed = 5

    already_guessed = []
    guesses_left = guesses_allowed
    num_won = 0

    guess = ""

    while guess != secret and guesses_left >= 1:

      lowest = int_check("low number: ")
      highest = int_check("Higher Number: ", lowest + 1)
      rounds = int_check("Rounds: ", 1)
      guess = int_check("Guess: ", lowest, highest)

      # checks that guess is not a duplicate
      if guess in already_guessed:
          print("You already guessed that number! Please try again "
                "You *still* have {} guesses left".format(guesses_left))
          continue

      guesses_left -= 1
      already_guessed.append(guess)

      if guesses_left >= 1:

          if guess < secret:
              print("Too low, try a higher number. Guesses left: {} ".format(guesses_left))
              
          elif guess > secret:
              print("Too high, try a lower number. Guesses left: {} ".format(guesses_left))
      else:
          if guess < secret:
              print("Too Low!")
          elif guess > secret: 
              print("Too High!")

      if guess == secret:
        if guesses_left == guesses_allowed - 1:
            print("Amazing! You got it ")
      else:
            print("Well done, you got it ")
# main routine





# End Summary
# Number of Guesses : What was the number : 