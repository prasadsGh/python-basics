readMe=open('example.txt','r').read()
#this will not work(below)
#readme=open('example.txt','r)
#readMe.read()
print(readMe)

readMe2=open('example.txt','r').readlines()
print(readMe2)