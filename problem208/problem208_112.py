# 解法1
# def main():
#   N, M = map(int, input().split())
#   num = [-1] * N

#   for _ in range(M):
#     s, c = map(int, input().split())
#     s -= 1
#     if s == 0 and c == 0:
#       if N != 1:
#         print(-1)
#         return
#     if num[s] == -1:
#       num[s] = c
#     elif num[s] != c:
#       print(-1)
#       return

#   ans = ""
#   for i in range(len(num)):
#     c = num[i]
#     if c == -1:
#       if i != 0 or N == 1:
#         ans += "0"
#       else:
#         ans += "1"
#     else:
#       ans += str(c)

#   print(ans)

# 解法2
def main():
  N, M = map(int, input().split())
  S = [0] * M
  C = [0] * M
  for i in range(M):
    s, c = map(int, input().split())
    S[i] = s-1
    C[i] = c

  if N == 1:
    start = 0
  else:
    start = 10 ** (N - 1)

  for n in range(start, 10 ** (N)):
    n = str(n)
    ok = True
    for i in range(M):
      s = S[i]
      c = C[i]
      if n[s] != str(c):
        ok = False
        break
    if ok:
      print(n)
      return

  print(-1)
main()
