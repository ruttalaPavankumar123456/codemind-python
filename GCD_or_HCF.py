n,m=map(int,input().split())
small=0
if n>m:
    small=m
else:
    small=m
for i in range (1,small+1):
    if (n%i==0) and (m%i==0):
        hcf=i
print(hcf)