# Code for B - Minor Change
# Use input() to fetch data from STDIN

s: str = input()
t: str = input()
ans: int = 0

for i in range(len(s)):
    if s[i] != t[i]:
        ans = ans + 1

print(ans)
