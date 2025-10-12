# Assignment: Simple Guess Game

# Custom function to run the game
def guess_game():
    secret_key = 7          # the number to guess
    attempts = 0            # counter
    max_attempts = 3        # total chances

    print("Welcome to the Guess Game 🎮")
    print("You have 3 chances to guess the correct number.")

    # while loop for attempts
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))  # built-in input()

        # check guess
        if guess == secret_key:
            print("🎉 You won ✅")
            return  # end the game if correct
        elif guess > secret_key:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        # increase attempts
        attempts += 1

    # if loop ends without correct guess
    if not (attempts < max_attempts) and guess != secret_key:
        print("❌ You lost! The correct key was", secret_key)

# Call the function
guess_game()
