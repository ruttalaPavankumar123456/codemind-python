n=int(input())
s=0
for j in range (1,n+1):
    s+=(1/j)
s="{:.2f}".format(s)
print(s)