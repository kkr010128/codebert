def fibonacci(n):
    a, b = 1, 0
    for _ in range(0, n):
        a, b = b, a + b
    return b

n=int(input())
n+=1
print(fibonacci(n))
