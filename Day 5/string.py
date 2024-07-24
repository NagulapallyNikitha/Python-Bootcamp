#string methods are is alpha, is digit,is alum,is upper,is lower,converting to lower case,converting to uppercase,title case,swap case
s=input()
print(s.upper())#---HELLO WORLD
print(s.lower())
print(s.title())#----Hello World
print(s.swapcase())#---convert the lower to upper 
print(s.capitalize())#-----Hello world
print(s.strip())#------remove the unwanted space
print(s.replace('a','z'))
print(s.split('l'))

#gives true or false

print(s.isdigit())#---- are 0-9
print(s.isalpha())#---check alphabets and no space then true or false
print(s.isalnum())#----check alphabeta and numeric
print(s.isnumeric())#---- all the numbers
print(s.isascii())
print(s.islower())
print(s.isupper())
print(s.istitle())