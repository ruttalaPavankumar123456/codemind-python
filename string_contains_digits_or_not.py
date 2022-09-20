t=int(input())
x=['0','1','2','3','4','5','6','7','8','9']
for j in range (t):
    y=str(input())
    s=0
    for j in range (len(y)):
        if y[j] in x:
            s+=1
        else:
            s=s
    if s==0:
        print('No')
    else:
        print('Yes')