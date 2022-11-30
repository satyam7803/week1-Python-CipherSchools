n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()


print(max(1,2,3,4,5,6,7))


n=6
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j) ,end=" ")
    print()


n=5
for i in range(n):
    for j in range(n):
        print(max(i,j) ,end=" ")
    print()