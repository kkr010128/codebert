import sys
input = sys.stdin.readline

m = [1, 1] + [None]*50

def fibonacci(n):
    if m[n-2]:
        pass
    else:
        fibonacci(n-2)
    if m[n-1]:
        pass
    else:
        fibonacci(n-1)

    m[n] = m[n-1] + m[n-2]

N = int(input())

fibonacci(44)
print(m[N])


