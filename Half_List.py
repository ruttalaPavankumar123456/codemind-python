n=int(input())
a=list(map(int,input().split()))
k=n//2
x=[]
y=[]
for j in range (0,k):
    x.append(a[j])
for i in range (len(a)):
    if a[i] not in x:
        y.append(a[i])
print(*(y[::-1]+x))