import os
import time
os.system("cls")
print("Welcome to Timer.org. You can set the countdown by entering how many hours, minutes, and seconds you want to use")
time.sleep(1)
a=int(input("How many Hours do you want to use?: "))
b=int(input("How many Minutes do you want to use?: "))
c=int(input("How many Seconds do you want to use?: "))
totalsecs=(a*60*60)+(b*60)+(c)
for i in range(totalsecs + 1):
    print("Total seconds left:")
    print(totalsecs-i)
    time.sleep(1)
    os.system("cls")
for i in range(999):
    print("DONE!!!")
    print(0000000)
    time.sleep(0.9)
    os.system("cls")
    time.sleep(0.5)
print("DONE!!!")