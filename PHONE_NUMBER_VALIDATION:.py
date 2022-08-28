x=int(input())
y=str(x)
if len(y)==10:
    temp=0
    for i in range(len(y)):
        if y[0]==0:
            temp=True
        else:
            temp=False
            
    if temp==True:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')