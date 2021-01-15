def bungusmungus():
    a=14
    doodle=[]
    for a in range(2000):
        if a%7==0 and a%5!=0:
            doodle.append(str(a))
            a=a+1
    print(", ".join(doodle))
    

bungusmungus()