a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    k=i
    i=str(i)
    for j in i:
        if j!="0" and k%int(j)==0:
            c+=1
    if c==len(i):
        print(k,end=" ")