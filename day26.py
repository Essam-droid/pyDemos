import os
import shutil 

path = source = "C:\\Users\\wwwmo\\Desktop\\temp\\azFiles\\"
destination = "C:\\Users\\wwwmo\\Desktop\\temp\\hopa\\"
os.chdir(path)

for file in os.listdir(path):

    if file.endswith(".txt"):
        #print(os.path.join(path, file))
        shutil.copy2(file , "../hopa" )
       