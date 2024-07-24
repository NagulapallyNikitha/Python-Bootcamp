#check how many vowels r there in a string
string=(input())
count=0
n="a","e","i","o","u"
for i in string:
    if(i in n):
        count+=1
print(count)