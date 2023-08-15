def pri(x):
    for i in range(2,int(x**0.5)):
        if x%i==0:
            return False
            break
    else:
        return True
a=int(input())
z=[]
for x in range(2,a//2):
    if a%x==0:
        y=a//x
        if (pri(x)==True) and (pri(y)==True):
            z.append(x)
            z.append(y)
            break
if z:
    print(*z)
else:
    print(-1)