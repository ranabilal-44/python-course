secret_key = 43
attempts = 3    
guess = int(input("Enter your guess: "))
if guess == secret_key:
    print("You won!")
else:
    guess = int(input("Wrong! Try again: "))
    if guess == secret_key:
        print("You won!")
    else:
        guess = int(input("Last chance! Enter your guess: "))
        if guess == secret_key:
            print("You won!")
        else:
            print("You lost! The correct key was", secret_key)