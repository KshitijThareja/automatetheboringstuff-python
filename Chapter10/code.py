import os, re, shutil
p= "/home/kshitij/automatetheboringstuff"
np= os.path.join(p, 'newfolder')
os.mkdir(np, 0o666)
try:
    for folderName, subfolders, filenames in os.walk(np):
        for filename in filenames:
            
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy( os.path.join(folderName,filename), "   /home/kshitij/automatetheboringstuff/newfolder")
except:
    print("No files with given extensions")

