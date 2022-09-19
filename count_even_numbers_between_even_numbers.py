n=int(input())
x=list(map(int,input().split()))
eve1=0
eve2=0
c=0
for i in range(len(x)):
    if x[i]%2==0:
        eve1=i
        break
for i in range(len(x)):
    if x[i]%2==0:
        eve2=i
for i in range(eve1+1,eve2):
        c+=1
print(c)