#we are gonna make a simple calculator

def addition(x,y):
    ans=(x+y)
    return ans
def multiplication(x,y):
    ans= (x*y)
    return ans
def division(x,y):
    ans=(x/y)
    return ans
def sub(x,y):
    ans=(x-y)
    return ans
a=2334

b=20

print("addition of the number: ")
print(addition(a,b))
print("multiplication of number:")
print(multiplication(a,b))
print("division of number")
print(division(a,b))
print("subtraction of a number ")
print(sub(a,b))
#if you are messing with the order of parameters--> assign values in the function calling itself for example
'''
def website(font, color , background color):
    
#calling function 
website(b=9000, a=12323122)





''' 