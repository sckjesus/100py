import sys, time, os

write = sys.stdout.write

def mungusaser():
    os.system("cls")
    for i in range(4):
        print("Loading"+"."*i)
        time.sleep(1)
        os.system("cls")   
    os.system("cls")
    print("Thanks for waiting!")
    time.sleep(1)
    os.system('cls')
    q=input('What is your username?: ')    
    c=["sanitha", "grapesK", "momosa", "nothing", "mookers" ]
    d=["bookman.kaspar/bookgen", "book.com", "seetha.o/momaseetha", "onum/illai", "blue"]
    if str(q) in c:
        if str(q)==c[0]:
            q=c[0]
            b=input("What is your password?: ")
        elif str(q)==c[1]:
            q=c[1]
            b=input("What is your password?: ")
        elif str(q)==c[2]:
            q=c[2]
            b=input("What is your password?: ")
        elif str(q)==c[3]:
            q=c[3]
            b=input("What is your password?: ")
        elif str(q)==c[4]:
            q=c[4]
            b=input("What is your password?: ")
        if str(b) in d:
            if str(q)==c[0]:
                q="Susanna"
            
            elif str(q)==c[1]:
                q="Grace"
                
            elif str(q)==c[2]:
                q="Samuel"
               
            elif str(q)==c[3]:
                q="Fladel"
            elif str(q)==c[4]:
                q="Christopher"
            print("Welcome "+q+"!")
    else:
        print("Please try again")
        q=input('What is your username?: ')    
        if str(q) in c:
            if str(q)==c[0]:
                q=c[0]
                b=input("What is your password?: ")
            elif str(q)==c[1]:
                q=c[1]
                b=input("What is your password?: ")
            elif str(q)==c[2]:
                q=c[2]
                b=input("What is your password?: ")
            elif str(q)==c[3]:
                q=c[3]
                b=input("What is your password?: ")
            elif str(q)==c[4]:
                q=c[4]
                b=input("What is your password?: ")
            if str(b) in d:
                if str(q)==c[0]:
                    q="Susanna"
                
                elif str(q)==c[1]:
                    q="Grace"
                    
                elif str(q)==c[2]:
                    q="Samuel"
                
                elif str(q)==c[3]:
                    q="Fladel"
                elif str(q)==c[4]:
                    q="Christopher"
                print("Welcome "+q+"!")
        
            else:
                print("Sorry, that's not correct. Unfortunately you are now locked out!")
        else:
            print("Sorry, that's not correct. Unfortunately you are now locked out!")
mungusaser()



