import math
c=0
a=int(input())
for i in range(a):
    a=int(input())
    b=math.sqrt(a)
    c=int(b)
    if c==b:
        print(True)
    else:
        print(False)