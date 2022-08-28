x=int(input())
z=x
y=x**2
pro=0
while y!=0:
    a=y%10
    pro+=a
    y//=10
if pro==z:
    print('Neon Number')
else:
    print('Not Neon Number')