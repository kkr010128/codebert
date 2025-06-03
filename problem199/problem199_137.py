S = input()

S_size = len(S)
S_hi = S.count('hi')

if S_size == S_hi*2:
    print('Yes')
else:
    print('No')