S = input()
K = int(input())



def func(S):
    inner = 0
    S = list(S)
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S[i + 1] = '#'
            inner += 1
    return inner

if len(set(list(S))) == 1:
    print(len(S) * K // 2)
else:
    inner = func(S)
    inter = func(S * 2) - func(S) * 2
    print(inner * K + inter * (K - 1))