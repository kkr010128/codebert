s = input()
ans = 0
for i in range(3):
    if s[i] == "R":
        ans = 1

for i in range(2):
    if s[i:i+2] == "RR":
        ans = 2

if s == "RRR":
    ans = 3

print(ans)
