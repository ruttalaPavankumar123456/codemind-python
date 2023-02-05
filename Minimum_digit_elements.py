n=int(input())
m=list(map(int,input().split()))
a=min(m)
cnt,b=0,0
for j in m:
    b=len(str(j))
    if b==len(str(a)):
        cnt+=1
print(cnt)