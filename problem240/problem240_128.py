N, M = map(int, input().split())

ac = wa = 0
ac_lis = [False] * N
wa_cnt = [0] * N
for _ in range(M):
  p, s = input().split()
  p = int(p) - 1

  if s == "AC":
    if not ac_lis[p]:
      ac += 1
      wa += wa_cnt[p]
      ac_lis[p] = True
  else:
    if not ac_lis[p]:
      wa_cnt[p] += 1

print(ac, wa)
