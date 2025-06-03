d = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(d)]
t = [int(input()) for i in range(d)]

def calc_score(day, contest, score, last):
  last[contest] = day + 1

  contest_score = s[day][contest]
  score += contest_score

  dis = 0
  for i in range(26):
    dis += c[i] * ((day + 1) - last[i])
  score -= dis

  return score, last


score = 0
last = [0 for i in range(26)]
for day in range(d):
  contest = t[day]
  contest -= 1
  score, last = calc_score(day, contest, score, last)
  print(score)