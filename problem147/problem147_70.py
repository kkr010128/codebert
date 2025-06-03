S = input()
T = input()
N = len(S)
if len(T) == N+1:
    Ts = T[:N]
    if Ts == S:
        print('Yes')
    else:
        print('No')
else:
    print('No')