s = input()
len_ = len(s)
half = len(s) // 2
ans = 0

if len_ % 2 == 0:
    front = s[:half]
    back = s[half:][-1::-1]
    for i in range(len(front)):
        if front[i] != back[i]:
            ans += 1
else:
    front = s[:half]
    back = s[half+1:][-1::-1]
    for i in range(len(front)):
        if front[i] != back[i]:
            ans += 1

print(ans)
