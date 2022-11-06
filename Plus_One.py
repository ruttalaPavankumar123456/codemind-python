a=int(input())
n=list(map(int,input().split()))
s=''
for j in n:
    s+=str(j)
s=str(int(s)+1)
for i in s:
    print(i,end=' ')