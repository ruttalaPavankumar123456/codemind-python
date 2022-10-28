x=int(input())
p=x
a=str(x)
m=len(a)
sp=0
for j in range (len(a)):
    z=x%10
    sp+=(z**m)
    m-=1
    x//=10
if sp==p:
    print(True)
else:
    print(False)