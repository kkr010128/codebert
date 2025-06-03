import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
a = [i for i in range(1,N+1)]
cnt = 0
ans_a, ans_b = 0, 0
for target in itertools.permutations(a):
    cnt += 1
    if list(target) == P:
        ans_a = cnt
    if list(target) == Q:
        ans_b = cnt
print(abs(ans_a-ans_b))