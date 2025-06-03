n = int(input())
l = list(sorted(map(int, input().split())))
x = 0
if n >= 3:
    for k in range(n - 2):
        for j in range(k + 1):
            for i in range(j + 1):
                if l[i] < l[j + 1] < l[k + 2] and l[i] + l[j + 1] > l[k + 2]:
                    x += 1
print(x)