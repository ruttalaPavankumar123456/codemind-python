n=int(input())
m=list(map(int,input().split()))
l=[]
for j in m:
    x=(j**2)
    l.append((x))
l.sort()
print(*l)