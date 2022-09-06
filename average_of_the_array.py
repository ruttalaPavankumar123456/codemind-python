n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range (len(a)):
    cnt+=a[i]
z=cnt/len(a) 
res="{:.2f}".format(z)
print(res)