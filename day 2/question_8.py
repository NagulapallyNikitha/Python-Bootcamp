#given an space seperated integer ,list find the average of elements present in the even 
list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(list)
for i in range(len(list)):
        sum+=list[i]
        count+=1
print(sum/count)
#write a program to find area of a circle 
#write a program to find perimete of a circle
#write a program to find area of a triangle
#write a program to find perimeter of a triangle
r=int(input())
pi=3.14
Area=pi*r*r
print(Area)
perimeter=2*pi*r
print(perimeter)
#new code
b=int(input())
h=int(input())
area=1/2*b*h
print(area)
a=int(input())
c=int(input())
perimeter=a+b+c
print(perimeter)



