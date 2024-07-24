#write a program to print all the consonants
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i=input()
inp=i.lower()
for i in inp:
    if(i in abc):
        count+=1
print(count)
#or
string=input()
count=0
n='a','e','i','o','u'
for i in string:
    if(i in n):
        count+=1
print(count)