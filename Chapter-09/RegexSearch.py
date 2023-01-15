import os
import re
a = input("Enter expression to be checked: ")
try:

    for file in os.listdir():
        if file.endswith(".txt"):
            with open(file, 'r') as f:
                data = f.read()
                exp = re.compile(a)
                find = exp.findall(data)

                for i in find:
                    item = i
                if item in data:

                    print(f"File {file} contains expression \"{item}\"")
except:
    print("Expression not matched")
