
list=list(map(int,input().split( )))
count=0
for i in range(1,len(list)-1):
    if(list[i]>list[i-1] and list[i]>list[i+1]):
        count=i
        #print(list,end=" ")
if(list[-1]>list[-2] and list[-1]>count):
    count=len(list)-1
print(list[count])