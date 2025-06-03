n = int(input())
s = input()
cnt = 0
for i in range(10):
    a = s.find(str(i))
    if a == -1:
        continue
    for j in range(10):
        b = s.find(str(j), a + 1)
        if b == -1:
            continue
        for k in range(10):
            c = s.find(str(k), b + 1)
            if c != -1:
                cnt += 1
print(cnt)