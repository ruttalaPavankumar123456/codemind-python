t=int(input())
for j in range(t):
    a=int(input())
    z=list(map(int,input().split()))
    cnt=0
    for i in range (a-1):
        if z[i+1]>=z[i]:
            cnt+=1
    if cnt == a-1:
        print('0')
    else:
        print(max(z)-min(z))