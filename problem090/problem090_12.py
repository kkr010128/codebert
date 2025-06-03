s = input()
counter = 0
ans = 0
for i in s:
    if i == "R":
        counter += 1
    else:
        counter = 0
    ans = max(ans, counter)
print(ans)