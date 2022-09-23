x=int(input())
while x>9:
    c=0
    while x:
        r=x%10
        c+=r
        x=x//10
    x=c
print(c)