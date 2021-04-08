# HL component 1 - get (and check) user input

# to do
# check a lowest is an integer (any integer)
# check that highest is more than lowest (lowest bound only)
# check that rounds is more than 1 (upper bound only)
# check that gues is between lowest and highest (
# lower and upper bound)


# number checking function goes here
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



# main routine

lowest = int_check("low number: ")