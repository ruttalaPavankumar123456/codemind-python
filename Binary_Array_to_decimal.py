n=int(input())
a=n-1
m=list(map(int,input().split()))
su=0
for j in range(n):
    su+=m[j]*(2**a)
    a-=1
print(su)