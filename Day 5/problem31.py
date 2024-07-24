#ABC 4
#EFG

s=input()
count=0
for i in s:
    print(chr(ord(i)+4,end=" "))
    count+=(i)
print(count)