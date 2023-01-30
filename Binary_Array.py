n=int(input())
cnt=0
m=list(map(int,input().split()))
for j in range(n):
    if m[j]==0 or m[j]==1:
        cnt+=1
if cnt==n:
    print(True)
else:
    print(False)