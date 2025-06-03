def ifTriangle(v):
    largest = max(v)
    smallers_sum = 0
    for x in v:
        if not x == largest:
            smallers_sum += x
    if smallers_sum > largest:
        return True
    return False


N = int(input())
L = [int(x) for x in input().split()]
L.sort()
L.reverse()

count = 0
before_i = -1
before_j = -1
before_k = -1
for i in range(N-2):
    for j in range(i+1, N-1):
        if L[j] == L[i]:
            continue
        if L[i]/2 >= L[j]:
            break
        for k in range(j+1, N):
            if L[k] == L[j]:
                continue
            if ifTriangle([L[i], L[j], L[k]]):
                count += 1
print(count)
