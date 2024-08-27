#This is a programe for improving my coding experience by creating a simple quiz game.

#Intro
print("Welcome to My Quiz!")

playing = input("\nWould you like to participate in the game? ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's Begin the Adventure :)")

score = 0
print("\n----- Current Score = "+str(score)+" -----")

#Question1
answer = input("\nQ01: Who is the father of Computer Science? ")
if answer.lower() == "charles babbage":
    print("You are Correct!")
    score += 10
else:
    print("You are Incorrect!")

#Question2
answer = input("\nQ02: What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("You are Correct!")
    score += 10
else:
    print("You are Incorrect!")

#Question3
answer = input("\nQ03: Coded entries which are used to gain access to a computer system are called? ")
if answer.lower() == "password":
    print("You are Correct!")
    score += 10
else:
    print("You are Incorrect!")

#Question4
answer = input("\nQ04: What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("You are Correct!")
    score += 10
else:
    print("You are Incorrect!")

#Question5
answer = input("\nQ05: A computer cannot 'boot' if it does not have the? ")
if answer.lower() == "operating system":
    print("You are Correct!")
    score += 10
else:
    print("You are Incorrect!")

print("\n\n------- Total score you achieved: "+ str(score)+" -------")
print("\n------- Total percentage you achieved: "+ str((score/50)*100)+"% -------")

print("\n***** Thank You for Playing the Quiz Game *****")