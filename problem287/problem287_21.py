n = int(input())
ans = []
for i in range(1, 10):
    for j in range(1, 10):
        ans.append(i * j)

print("Yes") if n in ans else print("No")
