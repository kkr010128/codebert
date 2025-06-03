S = input()

N = len(S)

S1 = S[:(N - 1) // 2]
S2 = S[(N + 3) // 2 - 1:]

def check(s):
    #print(s)
    i = 0
    j = len(s) - 1
    while j > i:
        if s[j] != s[i]:
            return False
        j -= 1
        i += 1
    return True


if check(S) and check(S1) and check(S2):
    print("Yes")
else:
    print("No")