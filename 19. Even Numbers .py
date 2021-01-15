def googly():
    a=input("Up to What number do you want to find even numbers?: ")
    b=[]
    if a.isdigit():
        for i in range(int(a)+1):
            if int(i)%2==0:
                b.append(str(i))           
    else:
        print("Try again")
        googly()
    print("The numbers you asked for are "+", ".join(b))
googly()


            
