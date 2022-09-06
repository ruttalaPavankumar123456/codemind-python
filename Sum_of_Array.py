n=int(input())
y=list(map(int,input().split()))
cnt=0
for i in range (len(y)):
        cnt+=y[i]
print(cnt)