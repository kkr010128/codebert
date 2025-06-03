S = input()
T = input()

s = len(S)
t = len(T)

T_1 = T[:-1]

if S == T_1:

    if t == s+1:
        print('Yes')

    else:
        print('No')

else:
    print('No')