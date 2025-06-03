N = int(input())
S = input()

count = 0
for p in range(10):
    s = S.find(str(p))
    if s == -1:
        continue
    for q in range(10):
        t = S.find(str(q), s + 1)
        if t == -1:
            continue
        for r in range(10):
            u = S.find(str(r), t + 1)
            if u != -1:
                count += 1
print(count)