import datetime

def gettime():
    return datetime.datetime.now()

def take(k):
    
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food : "))
        
        if(c==1):
            value=input("type here\n")
            with open("satish-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written..!!")
            
        elif(c==2):
            value = input("type here\n")
            with open("satish-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written..!!")
            
    elif(k==2):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        
        if (c == 1):
            value = input("type here\n")
            with open("Ashish-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written..!!")
            
        elif (c == 2):
            value = input("type here\n")
            with open("Ashish-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written..!!")
            
    elif(k==3):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        
        if (c == 1):
            value = input("type here\n")
            with open("Pradip-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written..!!")
            
        elif (c == 2):
            value = input("type here\n")
            with open("Pradip-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written..!!")
            
    else:
        print("Plz enter valid input (1(harry),2(rohan),3(hammad)")
        
        
def retrieve(k):
    
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        
        if(c==1):
            with open("satish-ex.txt") as op:
                for i in op:
                    print(i,end="")
                    
        elif(c==2):
            with open("satish-food.txt") as op:
                for i in op:
                    print(i, end="")
                    
    elif(k==2):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        
        if (c == 1):
            with open("Ashish-ex.txt") as op:
                for i in op:
                    print(i, end="")
                    
        elif (c == 2):
            with open("Ashish-food.txt") as op:
                for i in op:
                    print(i, end="")
                    
    elif(k==3):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        
        if (c == 1):
            with open("Pradip-ex.txt") as op:
                for i in op:
                    print(i, end="")
                    
        elif (c == 2):
            with open("Pradip-food.txt") as op:
                for i in op:
                    print(i, end="")
                    
    else:
        print("plz enter valid input (harry,rohan,hammad)")
        
        
        
print("Welcome to Health Management System: ")
a=int(input("Press 1 to log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for Satish 2 for Ashish 3 for Pradip "))
    take(b)
else:
    b = int(input("Press 1 for Satish 2 for Ashish 3 for Pradip "))
    retrieve(b)
