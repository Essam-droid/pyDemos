import sys
myword = input("please insert a string: ")
if len(myword) < 2:
    sys.exit()
else :    
    myword = myword[:2]+myword [-2:]
    print (myword)

