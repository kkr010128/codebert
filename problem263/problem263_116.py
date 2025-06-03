n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
MAX = 60

acc = [0] * MAX
ans = [0] * MAX

num = a[0]
for i in range(MAX):
    if num & 1:
        acc[i] = 1
    num >>= 1

for i, e in enumerate(a[1:], 1):
    for j in range(MAX):
        if e & 1:
            ans[j] += i - acc[j]
            acc[j] += 1
        else:
            ans[j] += acc[j]

        e >>= 1

ans_num = 0
for i, e in enumerate(ans):
    ans_num += pow(2, i, mod) * e
    ans_num %= mod

print(ans_num)
