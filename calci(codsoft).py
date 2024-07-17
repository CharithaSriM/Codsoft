num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
opr=str(input("Enter operation you want to perform : "))
if opr=="add":
    add=num1+num2
    print(num1,"+",num2,"=",add)
elif opr=="sub":
    sub=num1-num2
    print(num1,"-",num2,"=",sub)
elif opr=="mul":
    mul=num1*num2
    print(num1,"*",num2,"=",mul)
elif opr=="div":
    div=num1/num2
    print(num1,"/",num2,"=",div)
else:
    print("Selected operator doesn't exist")
