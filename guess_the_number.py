#Guess the number

import random
target= random.randint(1, 100)

while True:
    num = input("Guess the target number or Quit(Q):") #userinput
    if (num == "Q"): #check if it says quit
        break
    num = int(num) #change the input to integer
    if(num == target):  #check if user hits the target
        print("Your guessed number", num, "is correct")
        break
    elif(num > target):
        print("Your number was greater than target: Guess smaller number than", num)
    else:  
        print("Your number was less than target: Guess bigger number than", num)
print("---GAME OVER---")     










