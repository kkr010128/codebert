n = int(input())
list_ = []
for _ in range(n):
    x, l = map(int, input().split())
    list_.append([x-l, x+l])

list_.sort(key=lambda x: x[1])

res = n
pos = -float('inf')
for l, r in list_:
    if l < pos:
        res -= 1
    else:
        pos = r

print(res)