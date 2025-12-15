import random

num = random.randint(1, 100)

for i in range(1, 6):

    guess = int(input(f"Attempt {i}/5 - Guess the number: "))

    if guess == num:
        print(f"Congratulations!  You guessed the number in {i} tries!")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"Sorry, you've used all your attempts. The correct number was {num}.")
