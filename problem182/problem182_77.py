N, K, C = map(int, input().split())
S = input()
work_day_front = []
work_day_back = []

rest = 0
for i, c in enumerate(S):
    if rest > 0:
        rest -= 1
        continue

    if c == 'o':
        rest = C
        work_day_front.append(i)
max_work = len(work_day_front)

rest = 0
for i, c in enumerate(S[::-1]):
    if rest > 0:
        rest -= 1
        continue
    if c == 'o':
        rest = C
        work_day_back.append(N-i-1)

work_day_back = work_day_back[::-1]


if len(work_day_front) > K:
    print()
    exit()

ans = []
for i in range(len(work_day_back)):
    if work_day_back[i] == work_day_front[i]:
        ans.append(str(work_day_back[i]+1))
print("\n".join(ans))
