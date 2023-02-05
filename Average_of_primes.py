def prm(a):
    if a>1:
        cnt=0
        for j in range(2,a):
            if a%j==0:
                cnt+=1
        if cnt==0:
            return(a)
n=int(input())
z=list(map(int,input().split()))
su,cnt,avg=0,0,0
for j in z:
    if prm(j)==j:
        su+=j
        cnt+=1
avg="{:.2f}".format(su/cnt)
print(avg)