import os, re, shutil
p= "/home/kshitij/automatetheboringstuff"
np= os.path.join(p, 'newfolder')
type= input("Enter file type: ")
try:
    for folderName, subfolders, filenames in os.walk(p):
        for filename in filenames:
            
            if filename.endswith(type):
                isexist= os.path.exists(np)
                if isexist==True:
                    shutil.copy( os.path.join(folderName,filename), np)
                else:
                    os.makedirs(np)
                    shutil.copy( os.path.join(folderName,filename), np)

except:
    print("No files with given extensions")