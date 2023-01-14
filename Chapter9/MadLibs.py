import os
from pathlib import Path
import re

a= open('libs.txt', 'w')
a.write('SAMPLE TEXT \n The ADJECTIVE panda walked to the NOUN and then VERB. \n A nearby NOUN was unaffected by these events.')
a.close()

a= open('libs.txt', 'r')
data= a.read()
a.close()
aregex= re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
mo= aregex.findall(data)
for i in mo:
    if i=="ADJECTIVE" or i=="ADVERB":
        x= input(f"Enter an {i}: \n")
        f=data.replace(i,x,1)
        data=f
    else:
        x= input(f"Enter a {i}: \n")
        f=data.replace(i,x,1)
        data=f
print(data)
newfile= open('results.txt', 'w')
newdata= newfile.write(data)
newfile.close()
