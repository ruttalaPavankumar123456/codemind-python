n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
z=0
for j in a:
    if j%2==0:
        z+=1
print(z)