n=int(input())
l=list(map(int,input().split()))
s=0
for j in l:
    x=j
    z=x**0.5
    y=int(z)
    if y==z:
        s+=x
print(s)