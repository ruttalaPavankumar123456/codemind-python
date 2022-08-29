n=int(input())
a=n**2
b=str(n)
b=int(b[::-1])
m=b**2
c=str(m)
c=int(c[::-1])
if c==a:
    print(True)
else:
    print(False)