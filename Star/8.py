# r = 8
# c = 2*r

# for i in range(1,r+1) :
#     for j in range(1,c+1) :
#         if(j <= (c/2 - i) and j >= (c/2 + i-1)) :
#             print("*", end="")
#         else :
#             print("_", end="")
#     print(end="\n")
# afs

row=8

for i in range(row,0,-1):
    if(i==row):
        print("*"*(2*row),end="\n")
    else:
        print("*"*(i)+"_"*2*(row-i)+"*"*(i),end="\n")