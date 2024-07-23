#find GCD
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)
#find lcm,#lcm*gcd=a*b
a=int(input())
b=int(input())
c,d=a,b
#while b!=0:5
    #a,b=b,a%b
print((c*d)//a)