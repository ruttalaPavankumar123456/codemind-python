def prm(a):
    cnt=0
    for j in range(2,a):
        if a%j==0:
            cnt+=1
    if cnt==0:
        return a
        
t=int(input())
for j in range(t):
    x=int(input())
    m=x
    n=x
    while True:
        if prm(m)==m:
            print(m)
            break
        if prm(n)==n:
            print(n)
            break
        m-=1
        n+=1