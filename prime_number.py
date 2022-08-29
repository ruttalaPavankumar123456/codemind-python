x=int(input())
temp=0
for i in range (1,x+1):
    if i%1==0 and i%i==0 and i%2!=0 and i%3!=0:
        temp=True
    else:
        temp=False
if temp==True:
    print('prime')
else:
    print('not a prime')