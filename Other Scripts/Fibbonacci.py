#This is to script to check whether given number is in fibonacci sequence or not:

def Fibonacci():
    n = int(input("Enter the number you want to check : "))
    c = 0
    a = 1
    b = 1
    if n ==0 or n==1:
        print("Yes")
    else:
        while c<n:
            c = a+b
            b=a
            a=c
        if c==n:
            print("Yes")
        else:
            print("No")
Fibonacci()