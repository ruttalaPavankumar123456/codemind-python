t=int(input())
for i in range(t):
    x=int(input())
    y=str(x)
    rev=y[::-1]
    rev=int(rev)
    if x==rev:
        print(True)
    else:
        print(False)