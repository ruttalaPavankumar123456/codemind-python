n=int(input())
a=list(map(int,input().split()))
b=0
c=[]
for j in a:
    cnt=0
    b=str(abs(j))
    for k in range(len(b)):
        cnt+=1
    print(cnt,end=' ')