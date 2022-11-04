a=int(input())
while True:
    a+=1
    x=a
    y=str(x)[::-1]
    if x==int(y):
        cnt=0
        for j in range (2,x):
            if x%j==0:
                break
        else:
            print(x)
            break