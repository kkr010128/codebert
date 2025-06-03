def main():
  import bisect
  
  n = int(input())
  s = list(input())
  q = int(input())
  
  d = {}
  for i in range(26):
    d[chr(ord('a')+i)] = []
  for i in range(n):
    d[s[i]].append(i)
  #print(d)
  
  for i in range(q):
    t,a,b = input().split()
    if t == '1':
      a = int(a)-1
      if s[a] == b:
        continue
      #idx = bisect.bisect_left(d[s[a]],a)
      #d[s[a]].pop(idx)
      d[s[a]].remove(a)
      bisect.insort_left(d[b],a)
      s[a] = b
    else:
      a = int(a)-1
      b = int(b)-1
      c = 0
      for i in range(26):
        idx = bisect.bisect_left(d[chr(ord('a')+i)],a)
        if idx < len(d[chr(ord('a')+i)]) and d[chr(ord('a')+i)][idx] <= b:
          c += 1
      print(c)
  
main()