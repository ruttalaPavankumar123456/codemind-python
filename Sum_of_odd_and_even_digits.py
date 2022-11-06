n=int(input())
a=list(map(int,input().split()))
o=e=0
for j in range (len(a)):
    if j%2==0:
        e+=a[j]
    else:
        o+=a[j]
if (abs(e-o))==0:
    print('YES')
else:
    print('NO')