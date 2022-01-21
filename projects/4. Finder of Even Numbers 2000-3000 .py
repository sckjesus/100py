a=[]
for i in range(10000):
    if i>=2000 and i<=3000 and i%2==0:
       a.append(str(i))
print(",".join(a))