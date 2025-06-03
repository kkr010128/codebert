A, B, M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(M)]

ans = [min(a) + min(b)]
for x in X:
    a_idx, b_index, c = x
    ans.append(a[a_idx - 1] + b[b_index - 1] - c)

print(min(ans))