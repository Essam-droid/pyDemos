import time
import datetime

name = input("Enter your name")
num = input("Enter a number :")

num = int(num)

for i in range (num, 2, -1):
    print (i)
    time.sleep(1)
    if i == 5 :
        print ("The program is about to end")

time.sleep(1)
d = str(datetime.datetime.now())
print (name + '  '+ d)
