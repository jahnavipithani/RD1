import random
a=True
while(a):
    print(random.randint(1,6))
    print("Do you want to continue? y or n")
    i=input()
    if(i=='n'):
        a=False
    elif(i=='y'):
        a=True