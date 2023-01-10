#Date Detection

import re
dateregex= re.compile(r'(\d\d)/(\d{2})/(\d{4})')
mo= dateregex.search('34/02/3020')
day=str(mo.group(1))
month=str(mo.group(2))
year=str(mo.group(3))
if int(year)>=1000 and int(year)<=2999:

    if month in ["01", "03", "05", "07", "08", "10" "12"]:
        if int(day)<=31:
            print(mo.group())
        else:
            print("Doesn't Exist")

    if month in ["04", "06", "09", "11"]:
        if int(day)<=30:
            print(mo.group())
        else:
            print("Doesn't Exist")
    if month=="02":
        if ((int(year) % 400 == 0) or  
        (int(year) % 100 != 0) and  
        (int(year) % 4 == 0)) and int(day)<=29:
            print(mo.group())

        elif month=="02" and not ((int(year) % 400 == 0) or  
            (int(year) % 100 != 0) and  
            (int(year) % 4 == 0)) and int(day)<=28:
            print(mo.group())
        else:
            "Doesn't Exist"
else:
    print("Doesn't exist")


#Strong Password Detection

import re
passw = input("Enter a password : ")
try:
    passwregex= re.compile(r'\w{8,}')
    mo= passwregex.search(passw)
    a=mo.group()
    if len(a)<8:
        print("Password is weak")
    dig = any(chr.isdigit() for chr in a)
    upper= any(chr.isupper() for chr in a)
    lower= any(chr.islower() for chr in a)
    if dig and upper and lower:
        print("Password is strong")
    else:
        print("Password is weak")
except:
    print("Password is weak")


#Regex Version of the strip() Method

import re
def stripfn(str1,specchr):
    ask= input("Do you want to remoce specific characters from string? Y or N: ")
    if ask=="N":
        return str1.strip()
    else: 
        specchr= input("Enter character to be removed: ")
        str1regex= re.compile(specchr)
        return str1regex.sub("", str1)
specchr= ""
str1= input("Enter a string: ")
print(stripfn(str1, specchr))
    