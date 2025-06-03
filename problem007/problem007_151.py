target = int(input()) + 1
fib = [0 for n in range(target + 1)]
for i in range(target + 1):
    if i == 0:
        continue
    elif i == 1:
        fib[i] = 1
    else:
        fib[i] = fib[i - 1] + fib[i - 2]
print(fib[target])