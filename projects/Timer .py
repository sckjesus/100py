import os
import time
os.system("cls")
print("Welcome to Timer.org. You can set the countdown by entering how many hours, minutes, and seconds you want to use")
time.sleep(3)
a=int(input("How many Hours do you want to use?: "))
b=int(input("How many Minutes do you want to use?: "))
c=int(input("How many Seconds do you want to use?: "))
totalsecs=(a*60*60)+(b*60)+(c)
os.system("cls")
for i in range(totalsecs):
    print("Total hours/minutes/seconds left:")
    hours=str(int((totalsecs-i)/3600))
    minutes=str(int(((totalsecs-i)/60)%60))
    seconds=str(int((totalsecs-i)%60))
    print("Hours: "+hours+", Minutes: "+minutes+", Seconds: "+seconds)
    time.sleep(1)
    os.system("cls")
for i in range(999):
    print("DONE!!!")
    time.sleep(0.75)
    os.system("cls")
    time.sleep(0.75)
print("DONE!!!")