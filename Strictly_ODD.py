n=int(input())
m=list(map(int,input().split()))
a=0
b=0
for j in range(n):
    if j%2!=0 and m[j]%2!=0:
        a+=1
    if m[j]%2!=0:
        b+=1
if a==b:
    print(True)
else:
    print(False)