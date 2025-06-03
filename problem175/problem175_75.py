n = int(input())
s = input()
r, g, b = s.count("R"), s.count("G"), s.count("B")
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        try:
            k = j + (j - i)
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                cnt += 1
        except:
            pass
print(r * g * b - cnt)