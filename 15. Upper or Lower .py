def our_function():
    print(" ")
    a=input("Enter something: ")
    if a.isupper():
        print("This is uppercase ")
    elif a.islower():
        print("This is lowercase ")
    else: 
        print("Oops, something went wrong, try again")
        our_function()

our_function()
