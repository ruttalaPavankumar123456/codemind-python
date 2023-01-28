n=int(input())
x=64
for j in range(1,n+1):
    x+=1
    for i in range(n):
        print(chr(x),end=' ')
    print()