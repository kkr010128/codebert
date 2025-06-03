n = int(input())
a = [int(i) for i in input().split()]
max_a = max(a)
cnt_d = [0] * (max_a + 1)
for ai in a:
    for multi in range(ai, max_a + 1, ai):
        cnt_d[multi] += 1
print(sum(cnt_d[ai] == 1 for ai in a))