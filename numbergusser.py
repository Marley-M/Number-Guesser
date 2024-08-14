import random

while True:
    # stores the amount of tries a player has left
    tries = 4

    n = random.randrange(1, 10) # creates the goal number
    guess = int(input("Enter any number between 1 & 10: "))
    while n != guess:
        if guess < n:  # checks if number guesssed is lower than goal
            print(guess, "is too low!") # tells user that there guess is too low
            tries = tries - 1 # removes 1 try from there total left
            print("    Tries left:", tries) # prints the amount of tries user has left
            guess = int(input("Try again: "))
            if tries == 0: # checks if user is out of tries and if they are then tells them and starts the game over
                print(""" ⠀-GAME OVER-
-:OUT OF TRIES:-
""")
                break
        elif guess > n:  # checks if number guessed is higher than goal
            print(guess, "is too high!") # tells user that there guess is too high
            tries = tries - 1 # removes 1 try from there total left
            print("    Tries left:", tries) # prints the amount of tries user has left
            guess = int(input("Try again: "))
            if tries == 0: # checks if user is out of tries and if they are then tells them and starts the game over
                print(""" ⠀-GAME OVER-
-:OUT OF TRIES:-
""")
                break

    if guess == (n): # checks if user guessed correctly, if they did then it starts the game over
        print("""Correct, You guessed it right!!
        """)



