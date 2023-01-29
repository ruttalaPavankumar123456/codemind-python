def prm(a):
    cnt=0
    for j in range(2,a):
        if a%j==0:
            cnt+=1
    if cnt==0:
        return a
n=int(input())
x=n
y=n
if prm(n)==n:
    print('0')
else:
    while True:
        if prm(x)==x:
            print(abs(x-n))
            break
        if prm(y)==y:
            print(abs(y-n))
            break
        x+=1
        y-=1