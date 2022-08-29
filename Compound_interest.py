p,r,t=map(int,input().split())
i=p*(1+(r/100))**t
i="{:.2f}".format(i)
print(i)