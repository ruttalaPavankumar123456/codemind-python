n=int(input())
m=list(map(int,input().split()))
a=[]
b=0
for j in m:
    b=str(j)
    for k in range(len(b)):
        a.append(int(b[k]))
print(sum(a))