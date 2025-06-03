import random
import time
t_start = time.time()

d = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(d)]

def calc_score(day, contest, score, last):
  t_last = last[:]
  t_last[contest] = day + 1

  contest_score = s[day][contest]
  score += contest_score

  dis = 0
  for i in range(26):
    dis += c[i] * ((day + 1) - t_last[i])
  score -= dis

  return score


score = 0
last = [0 for i in range(26)]
for day in range(d):
  t_score = 0
  for each_contest in range(26):
    each_t_score = calc_score(day, each_contest, score, last)
    if each_t_score > t_score:
      t_score = each_t_score
      contest = each_contest

  score = t_score
  last[contest] = day + 1

  print(contest + 1)