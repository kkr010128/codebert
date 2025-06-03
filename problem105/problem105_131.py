# エイシング プログラミング コンテスト 2020: B – An Odd Problem
N = int(input())
a = [int(i) for i in input().split()]

num_odd = 0

for idx in range(1, N + 1, 2):
    if a[idx -1] % 2 == 1:
        num_odd += 1

print(num_odd)