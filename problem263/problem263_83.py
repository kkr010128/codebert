N = int(input())
A = list(map(int, input().split()))
num_list = [0] * 100
P = 10 ** 9 + 7
for i in A:
    tmp = i
    for j in range(len(bin(i)) - 2):
        num_list[j] += (tmp & 1)
        tmp = tmp >> 1
ans = 0


def func(N, n):
    return (N - n) * n


for i in range(100):
    ans = (ans + func(N, num_list[i]) * 2 ** i) % P
print(ans)
