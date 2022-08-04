a="My name is tony stark"
#to make all the letters of string upper case
s=a.upper()
print(s)
#to make all the letters of string lower case
b=s.lower()
print(b)

# to find the index of specific character

print(a.find('n'))
print(a.find("name"))

#for replacing some charater or string but it does not replace the original string 
s_1=a.replace("name","age")
s_2=b.replace('M','P')
print(s_1)
print(a)
print(s_2)

#to check whether the character or sunstring then :

print("name" in a)