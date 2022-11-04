n=int(input())
l=[]
l1=[]
cnt=0
for j in range (1,n+1):
    if n%j==0:
        l.append(j)
for i in range (len(l)):
    a=l[i]
    cnt=0
    for k in range (1,a+1):
        if a%k==0:
            cnt+=1
    if cnt!=2:
        l1.append(k)
print(len(l1))