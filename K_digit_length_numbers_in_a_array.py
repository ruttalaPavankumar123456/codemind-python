n,z=map(int,input().split())
m=list(map(int,input().split()))
cnt=0
for j in m:
    if z==len(str(abs(j))):
        cnt+=1
print(cnt)