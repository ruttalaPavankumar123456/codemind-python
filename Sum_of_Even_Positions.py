x=int(input())
y=list(map(int,input().split()))
cnt=0
for i in range (len(y)):
    if i%2==0:
        cnt+=y[i]
print(cnt)