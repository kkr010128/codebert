from time import time
import random

start = time()

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]


def cal_score(t):
  S = 0
  last = [-1] * 26
  score = 0
  for d in range(D):
    S += s[d][t[d]]
    last[t[d]] = d
    for i in range(26):
        S -= c[i] * (d - last[i])
    score += max(10 ** 6 + S, 0)
  return score
    
def main():
  t = [random.randint(0, 25) for _ in range(D)]
  score = cal_score(t)
  while time()-start + 0.2 < 2:
    d = random.randint(0, D-1)
    q = random.randint(0, 25)
    old = t[d]
    t[d] = q
    new_score = cal_score(t) 
    if new_score < score:
      t[d] = old
    else:
      score = new_score
  return t

if __name__ == "__main__":
  ans = main()
  for t in ans:
    print(t+1)