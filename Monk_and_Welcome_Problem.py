n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=[]
for j in range (len(x)):
    z=x[j]+y[j]
    a.append(z)
print(*a)