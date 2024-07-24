#print the unique characters in string 
string=input()
n='a','e','i','o','u'
abc="bcdfghjklmnpqrstvwxyz"
ans=" "
for i in string:
    if i not in ans:
        ans+=i
print(ans)
          
    
#sum of integer in a string
check="0123456789"
s="hello123"
ans=0
for i in s:
    if i in check:
        ans+=int(i)
print(ans)
        
#reverse the number present in a given string
check="0123456789"
s="hello1234world"
rev=0
while r!=0:
    rem=r%10
    r=r//10