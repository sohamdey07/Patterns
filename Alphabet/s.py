import string
ch = list(string.ascii_uppercase)
n= 5
k = 0
for i in range(1,n+1) :
    for j in range(0, i) :
        print(ch[k], end=" ")
        k += 1
    print(end="\n")
