N = int(input())
S = input()
total = S.count("R") * S.count("G") * S.count("B")
sub = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] == S[j]:
            continue
        h = j + j - i
        if h > N - 1 or S[j] == S[h] or S[h] == S[i]:
            continue
        sub += 1
print(total - sub)