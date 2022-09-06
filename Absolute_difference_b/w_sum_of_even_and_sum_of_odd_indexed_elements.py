n=int(input())
a=list(map(int,input().split()))
eve_sum=0
odd_sum=0
for i in range (len(a)):
    if i%2==0:
        eve_sum+=a[i]
    else:
        odd_sum+=a[i]
z=eve_sum-odd_sum
print(z)