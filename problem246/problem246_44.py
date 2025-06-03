import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

count = 1
for p in itertools.permutations(range(1, N+1)):

    if p == P:
        count_P = count
    if p == Q:
        count_Q = count

    count += 1

ans = abs(count_P - count_Q)
print(ans)