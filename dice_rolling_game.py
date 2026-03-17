import random

while True:
    dice = input("Roll the dice? (y/n): ").lower() #input what user want to do
    if dice == "n": #checks the input
        print("Thanks for playing!") #prints the statement
        break #break if it is true
    elif dice == "y":
        dice_number1 = random.randint(1,6) #choice a number from the list
        dice_number2 = random.randint(1,6)
        print(f"{(dice_number1, dice_number2)}")
    else: 
        print("Invalid Choice")
