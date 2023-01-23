n=int(input())
lst=list(map(int,input().split()))
m=max(lst)
while True:
    for i in range(n):
        if m%lst[i]!=0:
            break
    else:
        print(m)
        break
    m+=1