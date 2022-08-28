x=int(input())
temp=0
for i in range(x):
    if i*(i+1)==x:
        temp=True
    else:
        tem=False
if temp==True:
    print('YES')
else:
    print("NO")