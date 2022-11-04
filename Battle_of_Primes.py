a=int(input())
b=int(input())
c=a+b
x=0
for j in range(1,100):
    z=c+j
    cnt=0
    for i in range (2,z):
        if z%i==0:
            cnt+=1
    if cnt==0:
        x=j
        break
print(x)