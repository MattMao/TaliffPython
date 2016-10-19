"""
Santiago Lisa, Period 8, Roster 13
SAVE AS --> last first ___________.py

Write a short docstring here...

A guessing game that asks the user if he/she would like to continue, and does not allow out of bounds guesses.
"""


# ------------------------------------------
###########################################
# SECTION:  Import Modules As Needed
###########################################





# ------------------------------------------
###########################################
# SECTION:  Assign Constants and
#           Initialize ALL Variables
###########################################
# CONSTANTS     # FACTOR_BIOLOGY
# FACTOR_BIOLOGY = 0








# ------------------------------------------
# STRING VARIABLES
# nameStudent = " "     # initialize string
namePerson = ""
cont = "y"
colorGuess = ""
colorSecret = "blue"

# ------------------------------------------
# COUNTER VARIABLES
# countCells = 0        # integer
# countCars = 0         # integer
count = 0


# ------------------------------------------
# ACCUMULATOR (sum) VARIABLES
# sumChicken = 0        # integer
# accPieces = 0.0       # float
sumPoints = 0
sumGrades = 0.0


# ------------------------------------------
# MISCELLANEIOUS VARIABLES
# temporaryValue = 0.0
# temporaryName = ""
numberGuess = 0
numberSecret = 0





# ------------------------------------------
###########################################
# SECTION:  Welcome Message
###########################################





# ------------------------------------------
#******************************************
# SECTION:  Loop Header Begins Here
#******************************************
# ask for input (if needed) for loop
namePerson = input("What is your name? ")
numberSecret = 21
while True:
    count+=1
    for dumbLittleKid in range(2):
        numberGuess = int(input("Enter your guess: "))
        if numberGuess == numberSecret:
            print("Good job!")
    for dumbLittleKid in range(3):
        numberGuess = int(input("Enter your guess: "))
        if numberGuess == numberSecret:
            print("Good job!")
        else:
            print("Incorrect guess")
    for dumbLittleKid in range(4):
        numberGuess = int(input("Enter your guess: "))
        if numberGuess == numberSecret:
            print("Correct guess")
        elif numberGuess > 100:
            print("Over 100")
        elif numberGuess < 0:
            print("Under 0")
        elif numberGuess == 77:
            print("Number is 77") # TODO FIX THIS
            break
        else:
            print("Incorrect guess")
    for dumbLittleKid in range(3):
        numberGuess = int(input("Enter your guess: "))
        colorGuess = input("Enter your color guess").lower()
        if numberGuess == numberSecret and colorGuess == colorSecret:
            print("Correct number and color guess")
        else: # TODO FIX THIS ALSO
            print("Incorrect guess(es)")
    for dumbLittleKid in range(4): # TODO FIX THIS: LOOPS "INCORRECT" 8 TIMES
        if numberGuess == numberSecret or colorGuess == colorSecret:
            print("Correct number and color guess")
        elif numberGuess == numberSecret:
            print("Correct number guess")
        elif colorGuess == colorSecret:
            print("Correct color guess")
    cont = input("Continue? Type 'y': ")














# ------------------------------------------
#******************************************
# SECTION:  After Loop Ends
#           Calculations Here (if needed)
#******************************************








# ------------------------------------------
###########################################
# SECTION:  Display Summary Results Here
###########################################







# ------------------------------------------
###########################################
# SECTION:  Terminate the Program
###########################################
input("Press ENTER to quit.")
