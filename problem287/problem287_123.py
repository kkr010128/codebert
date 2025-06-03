N=int(input())
for i in range(10):
    for j in range(10):
        if N==i*j:
            print('Yes')
            exit()
print('No')