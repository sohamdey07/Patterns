n = 5
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if((i == 1 or i == 5) or (j == 1 or j == 5)) :
            print("1", end="")
        else :
            print("0", end="")
    print(end="\n")