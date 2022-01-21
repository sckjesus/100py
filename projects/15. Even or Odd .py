def our_function():
    print(" ")
    a=input("Enter a number: ")
    if a.isdigit():
        if int(a)%2==0:
            print("This is an even number")
        elif int(a)%2!=0:
            print("This is an odd number")
    else: 
        print("Oops, something went wrong, try again")
        our_function()
our_function()
