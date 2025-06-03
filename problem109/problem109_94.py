n = int(input())
ans_count = [0] * 4
ans = ['AC','WA','TLE','RE']

for s in range(n):
    tmp = input()
    for t in range(4):
        if tmp == ans[t]:
            ans_count[t] += 1

for s in range(4):
    print('%s x %d' % (ans[s],ans_count[s]))