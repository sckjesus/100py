a=input("Up to what number do you want numbers divisible by 5 and 7?: ")
b=[]
for i in range(int(a)+1):
    if int(i)%5==0 and int(i)%7==0:
        b.append(str(i))
print(",".join(b))
