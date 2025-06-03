ns = int(input())
s = list(map(int, input().split()))

nt = int(input())
t = list(map(int, input().split()))

count = 0

for i in t:
    # 配列に番兵を追加
    s += [i]
    j = 0
    while s[j] != i:
        j += 1
    s.pop()
    if j == ns:
        continue
    count += 1

print(count)

