import os

list1 = ['a','b','c','d','e']

os.chdir ("C:\\Users\\wwwmo\\Desktop\\temp\\")
os.mkdir("azFiles")
os.chdir ("C:\\Users\\wwwmo\\Desktop\\temp\\azFiles\\")

for i in range(len(list1)):
    open('%s.txt' % list1[i], 'w')