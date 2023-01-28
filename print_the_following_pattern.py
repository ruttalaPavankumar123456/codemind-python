n=int(input())
x=65+n
for j in range(1,n+1):
    x-=1
    for i in range(j,n+1):
        print(chr(x),end=' ')
    print()