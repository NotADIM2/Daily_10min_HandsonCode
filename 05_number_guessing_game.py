import random

secret = random.randint(1, 20)
attempts=0
max_attempts=5
won=False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20. You have 5 attempts to guess it.")

while attempts < max_attempts:
    try:
        guess = int(input("Take a guess: "))
        
        if guess < 1 or guess > 20:
            print("Please enter a valid number between 1 and 20.")
            continue
       
        attempts += 1
        if guess == secret:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            won = True
            break

        elif guess < secret:
            print("Your guess is too low.")

        else:
            print("Your guess is too high.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20.")

if not won:
    print("Sorry, you've used all your attempts. The number I was thinking of was", secret)
    print("Thank you for playing the Number Guessing Game!")