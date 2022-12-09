c=True
while c:
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Divisi0on\n5.Exit\n")
    print("Enter the number of operation")
    x=int(input())
    if x==5:
        break
    print("Enter your first number ")
    a=int(input())
    print("Enter your second number")
    b=int(input())
    
    if x==1:
        ans=a+b
        print(ans)
    elif x==2:
        ans=a-b
        print(a-b)
    elif x==3:
        ans=a*b
        print(ans)
    elif x==4:
        ans=a/b
        print(ans) 
    elif x==5:
        c=False
        break
    else:
        a="Enter the correct choice!!!" 
        print(a)  
    



