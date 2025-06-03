from collections import Counter

N = int(input())
A = list(map(int,input().split()))

count_a = Counter(A)
ans_list = [0] * (N+1)
for k, v in count_a.items():
    ans_list[k] = int(v * (v-1) / 2)

all_sum = sum(ans_list)
for i in range(N):
    print(all_sum - count_a[A[i]] + 1)
