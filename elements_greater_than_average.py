n=int(input())
a=list(map(int,input().split()))
su=sum(a)
avg=su//n
cnt=0
for j in range(n):
    if a[j]>=avg:
        cnt+=1
print(cnt)