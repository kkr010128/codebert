K = int(input())
S = str(input())

s_l = len(S)
s_k = list(S)
answer = s_k[slice(0, K)]
result = ''.join(answer)

if s_l <= K:
    print(S)

else:
    print(result + '...')