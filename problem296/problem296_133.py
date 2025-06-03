s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s) * k // 2)
    exit()

s += "🐧"

wow = 0
yeah = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        wow += 1
        yeah.append((s[i], wow))
        wow = 0
    else:
        wow += 1

ans = sum(c // 2 for _, c in yeah) * k

if s[0] == s[-2]:
    katakuna = yeah[0][1]
    ijippari = yeah[-1][1]
    te = katakuna // 2 + ijippari // 2 - (katakuna + ijippari) // 2
    ans -= te * (k - 1)

print(ans)