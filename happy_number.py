x=int(input())
while x>9:
    c=0
    while x:
        z=x%10
        c+=(z**2)
        x//=10
    x=c
if x==1 or x==7:
    print(True)
else:
    print(False)