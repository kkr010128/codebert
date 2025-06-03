N = int(input())

S, T = [x for x in input().split()]
result = []

while T:
    if len(S) == len(T):
        result.append(S[0])
        S = S[1:]
    else:
        result.append(T[0])
        T = T[1:]

print(''.join(result))
