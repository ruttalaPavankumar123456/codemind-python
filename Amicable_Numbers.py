m=int(input())
n=int(input())
count1=0
count2=0
for i in range(1,m):
    if (m%i)==0:
        count1+=i
    else:
        count1=count1
for j in range(1,n):
    if n%j==0:
        count2+=j
    else:
        count2=count2
if count1==n and count2==m:
    print('Amicable')
else:
    print('Not Amicable')