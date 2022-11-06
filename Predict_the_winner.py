a=int(input())
m=list(map(int,input().split()))
x=y=0
for j in range (len(m)):
    if j%2==0:
        x+=m[j]
    else:
        y+=m[j]
z=(abs(x-y))
if z%4==0:
    print('X')
else:
    print('Y')