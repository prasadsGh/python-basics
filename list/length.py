marks=[10,20,40,50,69,23,23]
a=len(marks)
print(a)
    
marks.insert(0,1234)
b=len(marks)
print(b)

# for i in marks:
#     print(i)
i=0
while i<len(marks):
    print(marks[i])
    i+=1