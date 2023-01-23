n=int(input())
lst=list(map(int,input().split()))
m=min(lst)
for i in range(m,0,-1):
    for j in range(n):
        if(lst[j]%i!=0):
            break
    else:
        print(i)
        break
    