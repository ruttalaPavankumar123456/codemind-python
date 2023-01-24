n=int(input())
a=''
for j in range (1,n+1):
    a+=str(j)
a=int(a)
for j in range(len(str(a))):
    print(a)
    a//=10