n=int(input())
a=list(map(int,input().split()))
l=[]
for j in a:
    x=j
    cnt=0
    for i in range (len(a)):
        if x>a[i]:
            cnt+=1
    l.append(cnt)
print(*l)