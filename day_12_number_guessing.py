import random


def number_guessing():
    print("Welcome to the guessing game!")
    comp_number = random.randint(1, 100)
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        print("You have 10 attempts. All the best!")
        for i in range(1, 11):
            guess = int(input("Guess the number: "))
            if guess == comp_number:
                print("You win!")
                break
            elif i == 10 and guess != comp_number:
                print("You lose!")
            elif guess != comp_number:
                if guess > comp_number:
                    print("Too high!")
                elif guess < comp_number:
                    print("Too low.")
                print("Try again!")
            else:
                print("Invalid.")
    elif difficulty == 'hard':
        print("You have 5 attempts. All the best!")
        for i in range(1, 6):
            guess = int(input("Guess the number: "))
            if guess == comp_number:
                print("You win!")
                break
            elif i == 10 and guess != comp_number:
                print("You lose!")
            elif guess != comp_number:
                if guess > comp_number:
                    print("Too high!")
                elif guess < comp_number:
                    print("Too low.")
                print("Try again!")
            else:
                print("Invalid.")

number_guessing()