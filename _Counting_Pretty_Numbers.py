n=int(input())
for i in range(n):
    l,r=map(int,input().split())
    count=0
    for j in range (l,r+1):
        
        z=j%10
        if z==2 or z==3 or z==9:
            count+=1
        else:
            count=count
        
    print(count)