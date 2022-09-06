n=int(input())
a=list(map(int,input().split()))
b=int(input())
cnt=0
for i in range (len(a)):
    if a[i]==b:
        cnt+=1
print(cnt)