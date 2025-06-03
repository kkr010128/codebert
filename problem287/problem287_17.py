N = int(input())
for i in range(1, 10):
    for k in range(1, 10):
        if(i*k == N):
            print('Yes')
            exit(0)
print('No')
