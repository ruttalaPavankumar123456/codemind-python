n=int(input())
if n>=0:
    res=int(str(n)[::-1])
else:
    a=abs(n)
    tmp=int(str(a)[::-1])
    res='-'+str(tmp)
    res=int(res)
print(res)