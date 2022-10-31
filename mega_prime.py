n=int(input())
lst=['2','3','5','7']
cnt=0
meg_prm=0
for j in range (2,n):
    if n%j==0:
        cnt+=1
if cnt!=0:
    print('Not Mega Prime')
else:
    temp=0
    a=str(n)
    for i in range (len(a)):
        if a[i] in lst:
            meg_prm+=1
    if meg_prm==len(a):
        temp=True
if temp==True:
    print('Mega Prime')
else:
    print('Not Mega Prime')