#print lower triangular matrix
for i in range(5):
    for j in range(5):
        if(i<=j):
            print("*",end="")
    print()
    
    
    
#print upper triangle matrix
for i in range(5):
    for j in range(5):
        if(i>=j):
            print("*",end="")
    print()