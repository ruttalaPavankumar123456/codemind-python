x=int(input())
pro=1
sum=0
while x!=0:
    z=x%10
    sum+=z
    pro*=z
    x//=10
y=pro-sum
print(y)