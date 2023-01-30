n=int(input())
m=list(map(int,input().split()))
cnt=0
for j in range(n):
    if m[j]%2==0:
        cnt+=1
if cnt==n:
    print(True)
else:
    print(False)