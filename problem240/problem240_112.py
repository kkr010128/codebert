N, M = map(int, input().split())
pena= 0
ac = [0]*(10**5)
for _ in range(M):
  tmp = input().split()
  if ac[int(tmp[0])-1] < 1:
    if tmp[1] == "AC":
      pena -= ac[int(tmp[0])-1]
      ac[int(tmp[0])-1] = 1
    else: ac[int(tmp[0])-1] -= 1 #penalty
print(ac.count(1), pena)