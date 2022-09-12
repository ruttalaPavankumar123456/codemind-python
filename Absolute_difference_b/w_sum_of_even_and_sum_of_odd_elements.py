n=int(input())
x=list(map(int,input().split()))
odd_sum=0
eve_sum=0
for i in range (len(x)):
    if x[i]%2!=0:
        odd_sum+=x[i]
    else:
        eve_sum+=x[i]
print(abs(odd_sum-eve_sum))