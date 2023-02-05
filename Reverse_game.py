n=int(input())
m=list(map(int,input().split()))
a=0
b=[]
for j in m:
    a=str(j)
    a=int(a[::-1])
    b.append(a)
print(*b,end='')
print()