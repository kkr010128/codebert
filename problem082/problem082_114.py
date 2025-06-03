s = input()
t = input()
ans = len(t)

for i in range(len(s) - len(t) +1):
    curr = len(t)
    for j in range(len(t)):
        if s[i+j] == t[j]:
            curr -= 1
    if curr < ans:
        ans = curr

print(ans)
