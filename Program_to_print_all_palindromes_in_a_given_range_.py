f=int(input())
l=int(input())
for x in range (f,l+1):
    y=str(x)
    z=int(y[::-1])
    if x==z:
        print(z,end=' ')