a=input("How many numbers do you want to square?: ")
a=int(a)
c=a+1
b=[]

for i in range(int(a)+1):
    b.append(str(str(i)+":"+str(int(i*i))))
print(" , ".join(b[1:c]))