n=int(input())
y=list(map(int,input().split()))
cnt=0
for i in range (len(y)):
    if y[i]%2!=0:
        cnt+=y[i]
print(cnt)