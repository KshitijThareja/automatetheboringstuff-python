**1.)**
With escape characters, we can use characters that we are otherwise unable to use in a string. An escape character consists of a backslash (\) followed by the character you want to add to the string. 

---
**2.)**
\n is used to give a new line in a text

\t is used to give a tab space

---
**3.)**
Using \\, i.e by escaping the '\' character.

---
**4.)**
Because the string is in double quotes. If it would have been inside single quotes, then we would have required the escape character.

---
**5.)**
For this, we can use a multiline string. Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.

---
**6.)**
a.) 'Hello, world!'[1] gives output as 'e'

b.) 'Hello, world!'[0:5] gives output as 'Hello'

c.) 'Hello, world!'[:5] Same as part b

d.) 'Hello, world!'[3:] gives output as 'lo, world!'

---
**7.)**
a.) 'Hello'.upper() gives output "HELLO"

b.) 'Hello'.upper().isupper() gives output True

c.) 'Hello'.upper().lower() gives output "hello"

---
**8.)**
a.) 'Remember, remember, the fifth of November.'.split()
 gives output-
 
 ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

b.) '-'.join('There can be only one.'.split()) gives output- 

There-can-be-only-one.

---
**9.)**
rjust() for right-justify

ljust() for left-justify

center() for center

---
**10.)**
For this we can use .strip() function.