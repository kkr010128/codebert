N = int(input())

ans = []
i = 1
while i * i <= N:
    if N % i == 0:
        x = i
        y = N / i
        ans.append(x+y-2)
    i += 1
print(int(min(ans)))
