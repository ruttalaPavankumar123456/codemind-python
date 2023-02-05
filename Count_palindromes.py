def pal(a):
    b=str(a)
    b=int(b[::-1])
    if a==b:
        return(a)
n=int(input())
m=list(map(int,input().split()))
cnt=0
for j in m:
    if pal(j)==j:
        cnt+=1
print(cnt)