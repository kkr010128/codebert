K = int(input())
A, B = [int(i) for i in input().split(' ')]
for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        exit()
print('NG')
