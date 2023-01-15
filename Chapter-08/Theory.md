**1.)**
PyInputPlus is not a part of the Python Standard Library. We have to install it using 'pip install --user pyinputplus'.

---
**2.)**
This is done to save us the trouble of writing the full name of the module whenever we need to use its functions.

---
**3.)**
inputInt() and inputFloat() take input in integer or floating point datatype resoectively.

---
**4.)**
For this we can use pyip.inputNum('>', min=0, lessThan=100)

---
**5.)**
The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

---
**6.)**
limit=3 restricts the input prompt to appear three times maximum in case the user enters an invalid input.

---
**7.)**
limit=3 restricts the input prompt to appear three times maximum in case the user enters an invalid input. And in case if the third input is also wrong, then the 'default' value declared is taken.