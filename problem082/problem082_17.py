s = input()
t = input()
ans = 1000

for idx in range(len(t), len(s)+1):
    tmp = 0
    for s_s, t_s in zip(list(s[idx-len(t):idx]), list(t)):
        if not s_s == t_s:
            tmp += 1
    if ans > tmp:
        ans = tmp

print(ans)