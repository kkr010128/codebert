N = int(input())
A = list(map(int, input().split()))
Q = int(input())
sum_res = sum(A)
counter = [0 for _ in range(10 ** 5 + 1)]

for a in A:
    counter[a] += 1

for _ in range(Q):
    B, C = map(int, input().split())
    sum_res = sum_res - (counter[B] * B)
    sum_res = sum_res + (counter[B] * C)
    counter[C] += counter[B]
    counter[B] = 0
    print(sum_res)
