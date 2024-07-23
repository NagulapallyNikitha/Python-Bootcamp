#find the maximum element in a given list
#12 23 36 44 45 57,56 78 -8 12 34 -99
#57,78
list=list(map(int,input().split(" ")))
max=list[0]
for i in range(len(list)):
    if(list[i]>max):
        max=list[i]
print(max)

        
    