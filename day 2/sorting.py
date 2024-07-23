my_list=list(map(int,input().split(",")))#list =typecasting,int=integer type,input=it is function,split is used for space
print(my_list)
#new code
my_list=list(map(int,input().split(",")))
for i in range(len(my_list)):
    print(my_list[i],end=" .")
    print("\n----------------")
    print(i,end=" ")
    s="helloworld"
    for i in range(len(s)):#while we r dealing with string we dont use range
        print(s[i],end=" ")
for i in s:
    print(i,end="")