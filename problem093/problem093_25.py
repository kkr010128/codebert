import sys
def main():
  input = sys.stdin.readline
  n, k = map(int , input().split())
  p_list = list(map(int, input().split()))
  c_list = list(map(int, input().split()))
  res = -float('inf')
  
  for s in range(n):
    S = []
    i = p_list[s] - 1
    S.append(c_list[i])
    while i != s:
      i = p_list[i]-1
      S.append(S[-1] + c_list[i])
    if k <= len(S):
      score = max(S[:k])
    elif S[-1] <= 0:
      score = max(S)
    else:
      score1 = S[-1] * (k//len(S) - 1)
      score1 += max(S)
      
      score2 = S[-1] * (k//len(S))
      r = k%len(S)
      if r!=0:
        score2 += max(0, max(S[:r]))
      score = max(score1, score2)
    res = max(res, score)
  print(res)
      

if (__name__=='__main__'):
  main()