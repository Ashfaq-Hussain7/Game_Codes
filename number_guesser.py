import random

top_of_range = input("\nEnter a number as limit: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("\nERROR!!! Please enter a number greater than ZERO next time.")
        quit()
else:
    print("\nERROR!!! Please enter a number next time.")
    quit()

random_no = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1 
    user_guess = input("\nMake a GUESS: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\nERROR!!! Please enter a number next time.")
        continue

    if user_guess == random_no:
        print("\nRandom number: "+ str(random_no))
        print("\nGuessed number: "+ str(user_guess))
        print("\n\n****** YOU WON!! You got it RIGHT. ******\n\n")
        break
    else:
        print("\nGuessed number: "+ str(user_guess))
        print("\nYou got it WRONG!!! TRY AGAIN.")

print("In", guesses, "guesses, you nailed it!")