import random as r1
x=r1.randrange(1,10)
name=input("Enter your name : ")
print("Welcome ",name,"to the guessing game.")
for i in range(1,11):
    guess=int(input("Enter any number between 1 to 10: "))
    print("Chance",i)
    if guess==x:
        print("Congratulations! You won.")
        break
    elif guess!=x:
        if guess>x:
            print("Please guess low.")
        else:
            print("Please guess high.")
    else:
        print("Invalid input")