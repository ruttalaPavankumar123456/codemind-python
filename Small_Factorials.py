n=int(input())
for i in range (n):
    x=int(input())
    p=1
    while x>0:
        p*=x
        x-=1
    print(p)