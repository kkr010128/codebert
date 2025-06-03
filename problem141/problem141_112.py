N = int(input())
A = list(map(int, input().split()))

if N == 0:
    if A[0] == 1:
        print (1)
        exit()
    else:
        print (-1)
        exit()


MAX = 10 ** 18
lst = [1] * (10 ** 5 + 10)

#純粋な2分木としたときの最大値
for i in range(N + 1):
    lst[i + 1] = min(MAX, lst[i] * 2)

# print (lst[:10])
for i in range(N + 1):
    tmp = lst[i] - A[i]
    if tmp < 0:
        print (-1)
        exit()
    lst[i + 1] = min(lst[i + 1], tmp * 2)

# print (lst[:10])

if lst[N] >= A[N]:
    lst[N] = A[N]
else:
    print (-1)
    exit()

# print (lst[:10])
ans = 1
tmp = 0
for i in range(N, 0, -1):
    ans += lst[i]
    lst[i - 1] = min(lst[i] + A[i - 1], lst[i - 1])

# print (lst[:10])
print (ans)
