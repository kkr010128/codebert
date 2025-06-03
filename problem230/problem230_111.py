def main():  
  import sys
  input = sys.stdin.readline
  n, d, a = [int(i) for i in input().split()]
  chk = []
  for i in range(n):
    x, h = [int(i) for i in input().split()]
    chk.append((x, 0, h))

  from heapq import heapify, heappop, heappush
  heapify(chk)
  atk_cnt = 0; ans = 0
  while chk:
    x, t, h = heappop(chk)
    if t == 0:
      if atk_cnt * a >= h:
          continue
      remain = h - atk_cnt * a
      new_atk = (remain - 1) // a + 1
      heappush(chk, (x + 2 * d, 1, new_atk))
      ans += new_atk
      atk_cnt += new_atk
    else:
      atk_cnt -= h
  print(ans)
if __name__ == '__main__':
    main()
