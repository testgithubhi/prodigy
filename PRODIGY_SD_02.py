import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()