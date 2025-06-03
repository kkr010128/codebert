S = input()
N = len(S)

one = S[:int((N-1) / 2)]
two = S[int((N+3) / 2)-1:]

if S == S[::-1]:
    if one == one[::-1]:
        if two == two[::-1]:
            print('Yes')
            exit()

print('No')
