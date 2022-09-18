n=int(input())
z=n
sum2=0
while n!=0:
    x=n%10
    y=1
    sum1=0
    while x!=0:
        y*=x
        x-=1
    sum1+=y
    n//=10
    sum2+=sum1
if sum2==z:
    print("The number",z,"is a strong number")
else:
    print('The number',z,'is not a strong number')