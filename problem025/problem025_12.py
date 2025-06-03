from itertools import combinations


n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


answer = ['no']*q
for i in range(1, n+1):
    for nums in combinations(a, i):
        val = sum(nums)
        if val in m:
            index = [i for i, num in enumerate(m) if val == num]
            for i in index:
                answer[i] = 'yes'

for i in answer:
    print(i)

