x=str(input())
a=0
b=0
for i in range (len(x)):
    if x[i]=='z':
        a+=1
    else:
        b+=1
if (b%(2*a))==0:
    print('Yes')
else:
    print('No')