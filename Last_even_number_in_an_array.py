n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range (len(a)):
    if a[i]%2==0:
        cnt=a[i]
print(cnt)