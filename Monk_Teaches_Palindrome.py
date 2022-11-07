a=int(input())
for j in range (a):
    x=input()
    y=x[::-1]
    if x==y:
        cnt=0
        n=0
        for i in range (len(str(x))):
            cnt+=1
        if cnt%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')
    else:
        print('NO')