import os

def split_file():

    var_in = input("Enter the text :")
    global first
    global second
    first = var_in[:int(len(var_in)/2)]
    second = var_in[int (len(var_in)/2):]


os.chdir ("C:\\Users\\wwwmo\\Desktop\\")
directory = input("Enter the directory name :")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
os.chdir (path)

split_file()

file1 = open ("first.txt","w+")
file1.write(first)
file2 = open ("second.txt","w+")
file2.write(second)

print (os.getcwd())

