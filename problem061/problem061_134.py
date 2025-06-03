S = input()

ans = ''
for s in S:
    ans += s.upper() if s.islower() else s.lower()
print(ans)
