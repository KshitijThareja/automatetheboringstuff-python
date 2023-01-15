#Input Validation

def collatz(number):
    
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number +1)
        return 3*number+1
count=0
while True:
    try:
        if count==0:
            number=int(input("Enter the number: "))
            c= collatz(number)
        # print(c)
            count+=1
        if count>0:
            c=collatz(c)

        if c==1:
            break
    except:
        print("Enter an integer")
