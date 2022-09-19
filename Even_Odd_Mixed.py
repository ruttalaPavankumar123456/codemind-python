x=int(input())
eve=0
odd=0
while x!=0:
     z=x%10
     if z%2==0:
        eve+=1
     else:
        odd+=1
     x//=10
if eve!=0 and odd==0:
    print('Even')
elif eve==0 and odd !=0:
    print('Odd')
else:
    print('Mixed')