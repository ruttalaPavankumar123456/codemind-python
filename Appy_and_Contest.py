t=int(input())
for j in range (t):
    n,a,b,k=map(int,input().split())
    cnt=0
    for i in range(1,n+1):
        if (i%a==0 and i%b!=0):
            cnt+=1
        elif (i%a!=0 and i%b==0):
            cnt+=1
        if cnt>=k:
            print('Win')
            break
    else:
        print('Lose')