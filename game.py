import random

print("Rock Paper Scissors Game")
print("Choose one: Rock, Paper, Scissors")

user_choice = input("Enter your choice: ").capitalize()

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("Result: It's a Tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Result: You Win!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("Result: You Win!")

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Result: You Win!")

else:
    print("Result: You Lose!")
