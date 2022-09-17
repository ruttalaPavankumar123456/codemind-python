a,b=map(int,input().split())
c=a*b
for i in range (2,c+1):
    if i%a==0 and i%b==0:
        break
print(i)
    