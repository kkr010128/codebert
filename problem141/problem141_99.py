N = int(input())
A = tuple(map(int, input().split()))
S = [0]
for a in reversed(A):
    S.append(S[-1] + a)
S.reverse()

lst = [0] * (N + 2)
lst[0] = 1
for i, a in enumerate(A):
    if lst[i] < a:
        print(-1)
        break
    lst[i + 1] = min((lst[i] - a) * 2, S[i + 1])
else:
    print(sum(lst))
