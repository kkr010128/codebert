
A,B,K=map(int, input().split())

if A >= K:
    print(f'{A-K} {B}')
elif (A+B) >= K:
    print(f'0 {B-(K-A)}')
else:
    print('0 0')