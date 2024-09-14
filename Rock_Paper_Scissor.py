import random

wins_of_user = 0
wins_of_computer = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nEnter a choice Rock/Paper/Scissors or E to EXIT: ").lower()
    if user_input == "e":
        quit("\nThank You!")
    
    if user_input not in options:
        continue 
    
    random_number = random.randint(0,2)
    #rock:0, paper:1, scissor:2

    computer_pick = options[random_number]
    print("\nThe Computer picked: ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("\nYou won!")
        wins_of_user += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("\nYou Won!")
        wins_of_user += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("\nYou won!")
        wins_of_user += 1
        
    else:
        print("\nYou Lost!")
        wins_of_computer += 1

print("\nYou won ", wins_of_user, "times.")
print("The Computer won ", wins_of_computer, "times.")
print("\nThank You And Goodbye!")
