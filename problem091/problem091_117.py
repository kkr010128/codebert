n = int(input())
l = list(map(int, input().split()))
t = 0

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            sum = l[i] + l[j] + l[k]
            if sum - max(l[i], l[j], l[k]) > max(l[i], l[j], l[k]):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                    t += 1

print(t)
