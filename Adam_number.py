x=int(input())
y=x**2
a=str(x)
m=int(a[::-1])
b=m**2
n=str(b)
z=int(n[::-1])
if z==y:
    print(True)
else:
    print(False)