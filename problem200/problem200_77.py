# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A, B, M = map(int, input().split())
List_A = list(map(int, input().split()))
List_B = list(map(int, input().split()))
List_discount = [list(map(int, input().split())) for i in range(M)]

# print(List_discount)
ans = 2 * 10**5
for d in List_discount:
    # print(d)
    p = List_A[d[0]-1] + List_B[d[1]-1] - d[2]
    ans = min(ans, p)
no_discount = min(List_A) + min(List_B)
ans = min(ans, no_discount)
print(ans)
