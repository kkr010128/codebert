n = int(input())
p = list(map(int, input().split()))

count = 0
m = p[0]

for i in p:
    m = min(m, i)
    if m == i:
        count += 1
print(count)