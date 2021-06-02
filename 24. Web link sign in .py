import sys, time, os

write = sys.stdout.write

def mungusaser():
    print("Loading...")
    for i in range(10):
        time.sleep(1)   
        write('\b')
    os.system('cls')
    print("Thanks for waiting!")
    time.sleep(1)
    os.system('cls')
    q=input('What is your username?: ')    
    c=["sanitha", "grapesK", "momosa", "nothing", "mookers" ]
    d=["bookman.kaspar/bookgen", "book.com", "seetha.o/momaseetha", "onum/illai", "blue"]
    if str(q) in c:
        if str(q)==c[0]:
            b=input("What is your password?: ")
        elif str(q)==c[1]:
            b=input("What is your password?: ")
        elif str(q)==c[2]:
            b=input("What is your password?: ")
        elif str(q)==c[3]:
            b=input("What is your password?: ")
        elif str(q)==c[4]:
            b=input("What is your password?: ")
        if str(b) in d:
            print("Welcome "+str(q.capitalize())+"!")
        else:
            print("Try again")
            if str(q) in c:
                if str(q)==c[0]:
                    b=input("What is your password?: ")
                elif str(q)==c[1]:
                    b=input("What is your password?: ")
                elif str(q)==c[2]:
                    b=input("What is your password?: ")
                elif str(q)==c[3]:
                    b=input("What is your password?: ")
                elif str(q)==c[4]:
                    b=input("What is your password?: ")
                if str(b) in d:
                    print("Welcome "+str(q.capitalize())+"!")
            else:
                print("Sorry, that's not corect, bye!")
            
mungusaser()



