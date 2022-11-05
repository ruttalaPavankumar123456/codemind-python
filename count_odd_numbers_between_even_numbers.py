n=int(input())
x=list(map(int,input().split()))
f_eve=0
l_eve=0
cnt=0
for j in range (len(x)):
    if x[j]%2==0:
        f_eve=j
        break
for i in range (len(x)):
    if x[i]%2==0:
        l_eve=i
for k in range (f_eve,l_eve):
    if x[k]%2!=0:
        cnt+=1
print(cnt)