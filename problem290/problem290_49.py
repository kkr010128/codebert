from math import ceil

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
F = sorted(list(map(int, input().split())))

def is_valid(A, F, K, T):
    for a, f in zip(A, F):
        if a*f > T:

            k = ceil(a - T/f)
            if k <= K:
                K -= k
            else:
                return False
    return True

def solve(N, K, A, F):
    i = 0
    left, right = 0, 10**12

    while left < right:
        mid = (left + right) // 2

        if is_valid(A, F, K, mid):
            right = mid
        else:
            left = mid + 1
    
    if is_valid(A, F, K, mid-1) and (not is_valid(A, F, K, mid)):
        return mid-1
    elif is_valid(A, F, K, mid):
        return mid
    else:
        return mid+1

print(solve(N, K, A, F))

