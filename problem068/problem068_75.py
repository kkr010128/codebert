w = input()
q = int(input())
for _ in range(q):
    S = input().split()
    s = S[0]
    a, b = map(int, S[1: 3])
    if s == "print":
        print(w[a: b + 1])
    elif s == "reverse":
        w = w[:a] + w[a: b + 1][::-1] + w[b + 1:]
    else:
        w = w[:a] + S[3] + w[b + 1:]
