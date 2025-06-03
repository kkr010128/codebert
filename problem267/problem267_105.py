n = int(input())
s = input()
ans = 0

for i in range(1000):
    i = str(i).zfill(3)
    a = s.find(i[0])
    if a != -1:
        b = s.find(i[1], a + 1)
        if b != -1:
            c = s.find(i[2], b + 1)
            if c != -1:
                ans += 1
print(ans)