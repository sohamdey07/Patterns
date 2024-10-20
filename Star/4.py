# for i in range(1,7) :
#     for j in range(1,i+1) :
#         print("*", end=" ")
#     print(end="\n")

row=6
for i in range(1,row+1):
    print("*"*i,end="\n")
print()

for i in range(row,0,-1):
    print("*"*i,end="\n")
    