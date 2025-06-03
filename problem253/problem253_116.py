N, A, B = map(int, input().split())
d = A - B if A > B else B - A
d2 = d // 2
d3 = d % 2
if d3 == 0:
  ans = d2
else:
  bigger = B
  smaller = A
  if A > B:
    bigger = A
    smaller = B
  shortest = smaller if N - bigger + 1 > smaller else N - bigger + 1
  ans = shortest + d2
  
  

print(ans)