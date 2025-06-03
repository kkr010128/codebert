N = int(input())
a = int(N / 1.08) # min
b = int((N + 1)  / 1.08) # max
ans = ':('
for i in range(a, b + 1):
    if int(i * 1.08) == N:
        ans = i
        break
print(ans)