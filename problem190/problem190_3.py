S = input()
N = len(S)


subS1 = S[:int((N - 1) / 2)]
subS2 = S[int((N + 3) / 2) - 1:]

if subS1 == subS1[::-1] and subS2 == subS2[::-1] and S == S[::-1]:
    print("Yes")
else:
    print("No")
