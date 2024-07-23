#printing the number
list=list(map(int,input().split(" ")))
count=0
for i in range(1,len(list),2):
    count+=1
print(count)
# ur given with a space seperated integer list find no. of even elements and odd elements in a given list
li=list(map(int,input().split(",")))
count=0
even=0
odd=0
for i in range(len(li)):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)