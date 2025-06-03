s = input()
t = input()

s_len = len(s)
t_len = len(t)

out = t_len

for i in range(0, s_len - t_len + 1):
    diff = 0
    for j in range(0, t_len):
        if t[j] != s[i + j]:
            diff += 1
    out = min(out, diff)

print(out)
