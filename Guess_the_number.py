import random 
target = random.randint(1,100)
while True:
    userChoice= int(input("Guess The Number: "))
    if(userChoice==target):
        print("Success: Correct Guess!!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger Guess..... ")

    else:
        print("Your number was too big. Take a smaller Guess.....")

print("______GAME OVER______")
