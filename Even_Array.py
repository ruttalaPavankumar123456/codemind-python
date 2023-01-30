n=int(input())
m=list(map(int,input().split()))
b=0
for j in range(n):
    if m[j]%2==0:
        b+=1
if n==b:
    print(True)
else:
    print(False)