import os, re, shutil
from pathlib import Path
a=input("Enter prefix of filename: ")
type= input("Enter file type(.txt, .pdf, etc): ")
folder= input("Enter folder's absolute path: ")
flist=[]
for file in os.listdir(folder):
    if file.endswith(type):
        # print(file)
        b= re.compile(fr'{a}\d\d\d')
        mo= b.findall(file)
        # print(mo)
        for i in mo:
            flist.append(i)
        flist.sort()
print(flist)
count=len(flist)
nums=[]
for item in range(1,count+1):
    filename= f"{a}{item:03}"
    last=flist[-1]
    if filename in flist:
        continue
    else:
        shutil.move(f"{folder}/{last}{type}", f"{folder}/{filename}{type}")
        flist.pop()



