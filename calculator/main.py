import math

print("this is the calculator made by @abhiraj-mishra with love❤️")

print("if you want the calculator to be basic type 1 else if want complex type 2")

type = int(input("1 or 2 : "))

if type == 1:
    print("the basic calculator is starting")
    nos = int(input("enter the no of numbers you want to operate with"))
    if nos == 2:
        print("the operator 1 for + , 2 for - , 3 for * , 4 for / ")
        operator=int(input("1,2,3,4 : "))
        if operator==1:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            print("the result is " , no1+no2)
        elif operator==2:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            print("the result is " , no1-no2)
        elif operator==3:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            print("the result is " , no1*no2)
        elif operator==4:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            print("the result is " ,no1/no2)
        else:
            print("koi dikkat ho gayi bro")
    if nos == 3:
        print("the operator 1 for + , 2 for - , 3 for * , 4 for / ")
        operator=int(input("1,2,3,4 : "))
        if operator==1:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            no3=int(input("no3 :"))
            print("the result is " , no1+no2+no3)
        elif operator==2:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            no3=int(input("no3 :"))
            print("the result is " , no1-no2-no3)
        elif operator==3:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            no3=int(input("no3 :"))
            print("the result is " , no1*no2*no3)
        elif operator==4:
            no1=int(input("no1: "))
            no2=int(input("no2: "))
            no3=int(input("no3 :"))
            print("the result is " ,no1/no2/no3)
        else:
            print("koi dikkat ho gayi bro")


elif type == 2:
    print("the advance calculator is starting")
    print("sorry for the incovience the advance calculator is building and will be available in next update")

