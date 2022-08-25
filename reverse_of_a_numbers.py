x=int(input())
y=0
rev=0
while x!=0:
    y=x%10
    rev=rev*10+y
    x//=10
print(rev)