#creation of list in python 
exampleList=[10,9,8,7,6,5,4,3,2,1,0]

for x in exampleList:
     print(x)
     
for things in exampleList:
    print(things)
print("----------------------------------------------------------------------------")

#for printing simple loops 
for i in range (1,10):
    print(i)
print("-----------------------------------------------------------------------------")
    
#for printing specific ranges only
# range(stop)
# range(start, stop[, step])
 
for i in range(1,10,2):
     print(exampleList[i])
print("-----------------------------------------------------------------------------")
#in next code we just stop at the given value 
for i in range(10):
    print(i)
print("-----------------------------------------------------------------------------")
for i in range(5):
    print(exampleList[i])
