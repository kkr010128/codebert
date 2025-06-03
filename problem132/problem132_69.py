N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(lst):
    for i in range(N):
        if lst[i] != N:
            return False
    return True

def move(lst):
    tmp = [0] * (N + 1)
    for i in range(N):
        a = lst[i]
        left = max(0, i - a)
        right = min(N, i + a + 1)
        tmp[left] += 1
        tmp[right] -= 1
    for i in range(N):
        tmp[i + 1] += tmp[i]
    return tmp

for i in range(K):
    A = move(A)
    if check(A):
        # print (i)
        break

print (*A[:-1])
