x=6

def fun():
    z=6
    print("this is z",z)
    print("this is x",x)
fun()
#x is global variable for all the variables under it 
#z is local variable under it 

#cannot do this 
#print(z) out of the function fun()
def example():
    global x;
    x+=1
    print(x)