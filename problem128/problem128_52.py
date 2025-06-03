x, n = list(map(int, input().split()))
q = list(map(int, input().split()))
p = [i for i in range(0, 102) if i not in q]

for i in range(len(p)):
    if p[i] < x:
        continue
    # p[i] >= x
    break

if p[i] == x:
    print(p[i])
else:
    if p[i] - x < x - p[i - 1]:
        print(p[i])
    else:
        print(p[i - 1])