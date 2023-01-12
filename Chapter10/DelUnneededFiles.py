import os, re, shutil
from pathlib import Path
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        a= os.path.getsize(os.path.abspath(filename))
        
        print(os.path.abspath(filename))