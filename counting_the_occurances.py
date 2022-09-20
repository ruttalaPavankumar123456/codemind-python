x=str(input())
c=str(input())
s=0
for i in range (len(x)):
    if x[i] == c:
        s+=1
if s==0:
    print('-1')
else:
    print(s)