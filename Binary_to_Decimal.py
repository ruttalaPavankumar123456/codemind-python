t=int(input())
for j in range (t):
    a=(input())
    a=a[::-1]
    b=0
    for k in range(len(a)):
        c=(int(a[k])*(2**(k)))
        b+=c
    print(int(b))