n = input()
ans = 0
temp = 0
for i in range(len(n)):
    if n[i] == "R":
        temp += 1
        ans = max(temp,ans)
    else:
        temp = 0

print(ans)