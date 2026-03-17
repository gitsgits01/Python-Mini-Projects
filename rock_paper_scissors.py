import random

ROCK ='r'
SCISSORS ='s'
PAPER = 'p'
emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️' }
r_s_p = tuple(emojis.keys())
def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s):").lower()
        if user_choice in r_s_p:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}",)
    print(f"Computer chose {emojis[computer_choice]}")

def determining_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
         print("Tie")
    elif(
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")
    else:
        print("You lose")
    
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice= random.choice(r_s_p)
        display_choices(user_choice, computer_choice)
        determining_winner(user_choice, computer_choice)
        c = input("Continue? (y/n): ").lower()
        if c == 'n':
            break
    
play_game()
    
    
         
   


