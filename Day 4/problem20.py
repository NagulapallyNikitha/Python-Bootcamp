#password verifier
#mr.x is trying to create a new password for an instagram account these r the required conditions  for cretaing a new password
#conditions:1.minimum length is 8 and maximum length is 15
#condition2:Only @,/ is allowed 
#condition3:no spaces are allowed
#condition4:only alpha numerics are allowed
#you are supposed to print weak:if length is exact 8,medium:length is between 8 to 12 strong:if length is between 12 to 15
string=input()
n='@/'
count=0
for i in string:
    if (i in n[0] or n[1] and i!=" ") :
        count+=1
        break
    else:
        print("follow the condition")
if(len(string)<8):
    print("follow the conditions")
elif(len(string)>8 and len(string)<12):
    print("password is strong")
elif(len(string)>12 and len(string)<15):
    print("password is strong")
else:
    print("password is weak")