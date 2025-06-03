from collections import Counter

N = int(input())
S = input()

counter = Counter(list(S))

ans = counter['R'] * counter['G'] * counter['B']

for d in range(1, N // 2 + 1):
    for a, b, c in zip(S, S[d:], S[2 * d:]):
        if a != b and b != c and c != a:
            ans -= 1

print(ans)
