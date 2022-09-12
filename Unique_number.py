n=int(input())
lst=[]
while n!=0:
    x=n%10
    lst.append(x)
    n//=10
res=list(set(lst))
if len(lst)==len(res):
    print('Unique Number')
else:
    print('Not Unique Number')