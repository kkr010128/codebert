line = list(input())
N = len(line)
i = 1
for i in range(N):
    if line[i] == "?":
        line[i] = "D"
print("".join(line))