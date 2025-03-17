import random

computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

user_choice = input("Do you want Rock, Paper, or Scissors: ")

print ('Computer choice is:', computer_choice)

if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice == 'Rock' and computer_choice == 'Scissors':
    print("You win!")
elif user_choice == 'Paper' and computer_choice == 'Rock':
    print("You win!")
elif user_choice == 'Scissors' and computer_choice == 'Paper':
    print("You win!")
else:
    print("You lose, computer wins")