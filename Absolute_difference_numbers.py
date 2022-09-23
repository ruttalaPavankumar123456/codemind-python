n,x=map(int,input().split())
m=str(n)
f=m[:x:]
l=m[len(m)-x:]
print(abs(int(f)-int(l)))