n=int(input())
x=list(map(int,input().split()))
avg=0
sum1=0
for i in range (len(x)):
    sum1+=x[i]
avg=(sum1//(len(x)))
if avg in x:
    print(True)
else:
    print(False)