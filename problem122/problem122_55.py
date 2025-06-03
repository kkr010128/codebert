n = int(input())
a = list(map(int, input().split()))
q = int(input())

s = sum(a)

arr = [0] * (10**5 + 1)
for i in range(n):
    arr[a[i]] += 1

ans = []
for i in range(q):
    b, c = map(int, input().split())
    nb = arr[b]
    bc = arr[c]
    s -= b * nb
    s += c * nb
    arr[b] = 0
    arr[c] += nb
    ans.append(s)

for i in range(q):
    print(ans[i])