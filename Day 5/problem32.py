#input=hello-----world,hello-----wor----ld
#output=-----hello world,---------helloworld


s=input()
count=0
r=" "
for i in s:
    if i=='-':
        count+=1
print(count)  
for i in s:      
    if(ord[i]>=96 and ord[i]<=12):
        r+=i
print('-'*count+r)