K = int(input())
A, B = map(int, input().split())

for i in range(1000):
    C = K * i
    if A <= C and C <= B:
        print('OK')
        exit()
    
print('NG')