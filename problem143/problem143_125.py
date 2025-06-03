K = int(input())
S = input()

len_S = len(S)

if len_S <= K:
    print(S)
else:
    print(S[:K] + '...')