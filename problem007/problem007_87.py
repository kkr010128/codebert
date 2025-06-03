n = int(input().strip())
if n <= 1:
    print(1)
    raise SystemExit
prev1 = 1
prev2 = 1
for i in range(2, n+1):
    fib = prev2 + prev1
    prev2, prev1 = prev1, fib
print(fib)