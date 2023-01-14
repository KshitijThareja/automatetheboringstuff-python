**1.)**
assert spam<10

---
**2.)**
eggs="SomeThing"
bacon="SOMETHING"
a=var1.upper()
b=var2.upper()
assert a==b

---
**3.)**
assert 1==0

---
**4.)**
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s -  %(message)s')

---
**5.)**
import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')

---
**6.)**
The five logging levels are debug, info, warning, error, and critical.

---
**7.)**
logging.disable() function, with a suitable logging level, can be used to disable logging messages for a program.

---
**8.)**
As it is tedious to remove all the print messages one by one, we prefer the logging messages more. We can disable the logging messages with a single line of code, i.e logging.disable() function. While removing print messages after debugging, we might even accidentally remove some print() calls that were being used for nonlog messages.

---
**9.)**
STEP IN- Clicking the Step In button will cause the debugger to execute the next line of code and then pause again. If the next line of code is a function call, the debugger will “step into” that function and jump to the first line of code of that function.

STEP OVER- It is similar to the Step In button. However, if the next line of code is a function call, The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns. 

STEP OUT- Clicking the Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.

---
**10.)**
It stops only on reaching a breakpint or at termination of code.

---
**11.)**
A breakpoint forces the debugger to pause whenever the program execution reaches a particular line.

---
**12.)**
By clicking on the line number in the editor, we can set a breakpoint, which can be confirmed from the red dot which appears on that line.