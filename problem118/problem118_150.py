N = int(input())

total = 0
for n in range(1, N+1):
    total += N//n * (n + N - N%n)//2

print(total)
