A,B,C,K = [int(x) for x in input().split()]
result = 0
if K > A:
    result += A
else:
    print(K)
    exit()

if K < A + B:
    print(result)
    exit()

print(result - (K - A - B))