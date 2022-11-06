a=int(input())
n=list(map(int,input().split()))
for j in range (len(n)):
    x=n[j]
    s=1
    for i in range (len(n)):
        if x!=n[i]:
            s*=n[i]
    print(s,end=' ')