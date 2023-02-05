n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for j in a:
    if j%k!=0:
        cnt+=1
print(cnt)