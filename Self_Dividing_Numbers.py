a=int(input())
b=int(input())
for x in range(a,b+1):
    z=x
    c=0
    while x:
        r=x%10
        if r==0:
            x=x//10
            continue
        elif z%r==0:
            c+=1
        x=x//10
    if len(str(z))==c:
        print(z,end=" ")
        
        