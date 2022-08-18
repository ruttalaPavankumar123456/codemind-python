x=int(input())
num=0
while x!=0:
    y=x%10
   
    x//=10
    if num<y:
         num=y
print(num)