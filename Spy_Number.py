x=int(input())
s=0
p=1
while x!=0:
    y=x%10
    s+=y
    p*=y
    x//=10
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')