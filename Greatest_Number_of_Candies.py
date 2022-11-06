n=int(input())
m=list(map(int,input().split()))
a=int(input())
x=[]
l=[]
for j in m:
    b=j+a
    x.append(b)
for i in x:
    y=i
    cnt=0
    for k in range (len(m)):
        if y>=m[k]:
            cnt+=1
    if cnt==(len(m)):
        l.append(True)
    else:
        l.append(False)
print(*l)