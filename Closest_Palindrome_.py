def pal(a):
    b=int(str(a)[::-1])
    if a==b:
        return(a)

n=int(input())
c=0
d=0
for j in range (1,100):
    m=n+j
    if pal(m)==m:
        c=m
        break
for k in range (1,100):
    x=n-k
    if pal(x)==x:
        d=x
        break
if (abs(n-c))==(abs(n-d)):
    print(d,c)
elif (abs(n-c))>(abs(n-d)):
    print(d)
else:
    print(c)