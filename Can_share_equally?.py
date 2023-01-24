x,y=map(int,input().split())
z=2*y
if ( x%2==0 and (x!=0 or y%2==0)):
    print('YES')
else:
    print('NO')