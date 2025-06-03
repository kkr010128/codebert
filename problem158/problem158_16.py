K = int(input())
A, B = map(int, input().split())
exist = False
for i in range(A, B+1):
    if i % K == 0:
        exist = True
print('OK' if exist else 'NG')