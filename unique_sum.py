n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
su=0
for j in a:
    su+=j
print(su)