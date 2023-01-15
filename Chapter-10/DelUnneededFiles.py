import os, re, shutil
from pathlib import Path
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        # print(filename)
        a= os.path.getsize(os.path.join(folderName,filename))
        # print(os.path.join(folderName, filename))
        if a>104857600:
            print(filename, "is of size ", a//104857600, "MB with path: ", os.path.join(folderName,filename))
            
