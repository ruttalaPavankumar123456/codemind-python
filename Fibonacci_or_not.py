n=int(input())
a=0
b=1
l=[]
l.append(a)
l.append(b)
for j in range (n):
    c=a+b
    a=b
    b=c
    l.append(c)
if n in l:
    print(True)
else:
    print(False)