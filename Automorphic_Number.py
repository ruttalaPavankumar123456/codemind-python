n=int(input())
n1=str(n)
m=n**2
m1=str(m)
x=10**(len(n1))
y=m%x
y=int(y)
if n==y:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
