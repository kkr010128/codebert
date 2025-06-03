S = list(input())
K = int(input())
L = len(S)

if len(set(S)) == 1:
    print(L*K // 2)
    exit()

def n_changes(s):
    sc = s.copy()
    count = 0
    for i in range(1, len(sc)):
        if sc[i] == sc[i-1]:
            sc[i] = "X"
            count += 1
    return count

print(n_changes(S) + (K-1) * (n_changes(2*S) - n_changes(S)))
