n = int(input())
c = list(input())

x = c.count("R")

ans = 0
for i in range(x):
    if c[i] == "W":
        ans += 1

print(ans)