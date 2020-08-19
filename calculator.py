#Program to make a simple calculator
#import math
print("\t________calculator__________")

def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
      a-=b
      return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("\tThe quotient is :",q)
    print("\tThe remainder is :", r)

def sqr(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\n\nChoose thr operation you want to perform:")
    print("\n\t1.ADDATION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MLTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SOUARE ROOT")
    print("\n\t6.EXIT")

    choice=int(input(">"))
    if choice==1:
        print("\n\nEnter the two number :")
        num1=int(input(">"))
        num2=int(input(">"))
        s=num1+num2
        print("The sum is :",s)
    elif choice == 2:
        print("\n\nEnter the two number :")
        num1 = int(input(">"))
        num2 = int(input(">"))
        m= num1-num2
        print("The differnce is:", m)
    elif  choice == 3:
        print("\n\nEnter the two number :")
        num1 = int(input(">"))
        num2 = int(input(">"))
        p = mul(num1, num1)
        print("The product is :", p)
    elif choice==4:
        print("\n\nEnter the two number :")
        num1 = int(input(">"))
        num2 = int(input(">"))
        d = div(num1, num1)
        print("The  division is :",d)
    elif choice==5:
        print("\n\nEnter the  number :")
        num1 = int(input(">"))
        r=sqr(num1)
        print("The sqr root is is :", r)
    else:
        print("\nYou choose to exit Bye.......")
        break





