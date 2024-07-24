print(ord('A'))
print(chr(65))
for i in range(32,128):
    print(chr(i),end=" ")

#print the ascii values
s=input()
sum=0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)
#write a code to print all the capital letters in a given string
s=input()
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        print(i)
        
        
#remove all the brackets from the given algebric expression
s=input()
for i in s:
    if (ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123  or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print()