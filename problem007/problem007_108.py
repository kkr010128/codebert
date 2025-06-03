n = int(input())

fib = []
ans = 0
for i in range(n+1):
    if i == 0 or i == 1:
        ans = 1
        fib.append(ans)
    else:
        ans = fib[i-1] + fib[i-2]
        fib.append(ans)

print(ans)
