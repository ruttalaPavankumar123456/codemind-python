x=str(input())
y=['0','1','2','3','4','5','6','7','8','9']
s=0
for i in range (len(x)):
    if x[i] in y:
        s+=int(x[i])
print(s)