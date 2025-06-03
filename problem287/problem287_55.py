n=int(input())
for i in range(9):
    for j in range(9):
        k = (i+1)*(j+1)
        if n==k:
            print('Yes')
            exit()
        else:
            continue
print('No')