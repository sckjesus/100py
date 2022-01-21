import random
from random import randint
def guesser():
    a=randint(1,100)
    print("Lets play the number guessing game!")
    b=input("Guess the number: ")
    if int(b)==a:
        print("Correct on the first try!!!")
        print("Congratulations!")
    else:
        while int(b)!=a:
            if int(b)>a:
                print("The number is lower than that")
            elif int(b)<a:
                print("The number is higher than that")
            b=input("Try again: ")
            if str(b)=="stop":
                break
            if b.isdigit():
                if int(b)==a:
                    print("Correct!!!")
                    print("Congratulations!")
                    print("Woohoooo!!!")
                    guesser()
guesser()