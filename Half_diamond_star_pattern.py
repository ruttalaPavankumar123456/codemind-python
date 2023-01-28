x=int(input())
if x<=2:
    print('The pattern is not possible')
else:
    for j in range (1,x+1):
        for i in range(1,j+1):
            print('*',end='')
        print()
    for j in range (x-1,0,-1):
        for i in range(j):
            print('*',end='')
        print()