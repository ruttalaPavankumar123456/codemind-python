n=int(input())
x=list(map(int,input().split()))
f_odd=0
l_odd=0
cnt=0
for j in range (len(x)):
    if x[j]%2!=0:
        f_odd=j
        break
for i in range (len(x)):
    if x[i]%2!=0:
        l_odd=i
for k in range (f_odd,l_odd):
    if x[k]%2==0:
        cnt+=1
print(cnt)