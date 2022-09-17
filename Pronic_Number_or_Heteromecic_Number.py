n=int(input())
for i in range (1,n+1):
    if (i*(i+1))==n:
        temp=True
        break
    else:
        temp=False
if temp==True:
    print("YES")
else:
    print('NO')