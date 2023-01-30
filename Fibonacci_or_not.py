i=0
j=1
su=0
n=int(input())
m=0
while True:
    su=i+j
    i=j
    j=su
    if su==n:
        m=True
        break
    if su>n:
        break
if m==True:
    print('True')
else:
    print('False')