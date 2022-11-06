a=int(input())
x=list(map(int,input().split()))
c=0
for j in x:
    m=j
    if len(str(m))%2==0:
        c+=1
print(c)