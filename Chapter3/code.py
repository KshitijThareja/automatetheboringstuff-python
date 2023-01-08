#The Collatz Sequence

def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number +1)
        return 3*number+1

while True:
    n=int(input("Enter the number: "))
    c= collatz(n)

    if c==1:
        break


#Input Validation

def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number +1)
        return 3*number+1

while True:
    try:

        n=int(input("Enter the number: "))
        c= collatz(n)

        if c==1:
            break
    except:
        print("Enter an integer")