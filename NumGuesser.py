import random

def game_loop(): 
    numToGuess = random.randint(1,100)
    attempts = 0

    print("Guess whole number from 1 to 100")

    while True:
        rawGuess = input("Enter Guess: ").strip()

        if not rawGuess.isdigit():
            print("Enter a valid nonzero positive int")
            continue

        guess = int(rawGuess)
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.\n")
            attempts -= 1
            continue

        