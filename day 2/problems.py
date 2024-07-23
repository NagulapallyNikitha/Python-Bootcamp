list=list(map(int,input().split(",")))
print("*********\n1.append\n 2.pop\n 3.sort\n 4.length of list\n***********")
print("enter the choice ")
choice=int(input())
if(choice==1):
   print(list)
elif(choice==2):
    list.pop()
    print(list)
elif(choice==3):
    list.sort()
    print(list)
elif(choice==4):
    print(len(list))
    print(list)
#new code
#PRINT 1 TO 100 NO. USING FOR LOOP
#USINg FOR LOOP APPEND 1TO 100 NO. INA AN EMPTYLIST
#FIND SUM OF ALL THE NO. INA LIST
#new code
n=int(input())
for i in range(1,n):
    print(i,end=" ")
#new code
list=[]
n=int(input())
for i in range(1,n+1):
    list.append(i)
print(*list)
#new code
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

    

