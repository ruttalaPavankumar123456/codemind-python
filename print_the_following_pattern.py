n=int(input())
s=[]
for j in range(n,0,-1):
    s.append(j)
for i in range(n):
    print(*s,end=' ')
    print()