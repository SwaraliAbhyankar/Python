import random
n = random.randint(1, 10)
guess = 0

while guess != n:
    guess = int(input("Enter your guess: "))

    if guess < n:
        print("Your number is small")
    elif guess > n:
        print("Your number is big")
    else:
        print("Correct guess!")

#Program for guessing the number with limited trials is in GUESS IT