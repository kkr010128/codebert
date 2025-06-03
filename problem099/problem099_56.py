N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_cuttable(N):
    n = 0
    for a in A:
        i = a // N
        if a % N == 0:
            i -= 1
        n += int(i)
        if n > K:
            return False
    return True

n_max = 10 ** 10
n_min = 0

while n_max - n_min > 1:
    n = (n_max + n_min) // 2
    if is_cuttable(n):
        n_max = n
    else:
        n_min = n
    
print(n_max)