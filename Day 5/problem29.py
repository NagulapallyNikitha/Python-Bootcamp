#print all the vowels followed by consonants
n='a','e','i','o','u'
abc="bcdfghjklmnpqrstvwxyz"
ans=""
i=input()
inp=i.lower()
for i in inp:
    if(i in n):
        ans+=i
        
for i in inp:
    if(i in abc):
        ans+=i
print(ans)        