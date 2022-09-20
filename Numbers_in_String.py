x=str(input())
s=0
y=['0','1','2','3','4','5','6','7','8','9']
for i in range (len(x)):
    if x[i] in y:
        s+=int(x[i])
print(s)