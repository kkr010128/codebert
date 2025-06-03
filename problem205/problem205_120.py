def main():  
  import sys
  input = sys.stdin.readline
  n,p = [int(i) for i in input().split()]
  s = input()
  ans = 0
  import collections
 
  if p == 2 or p == 5:
      for i in range(n):
          if int(s[i]) % p == 0:
              ans += i + 1
      print(ans)
      exit()
 
  else:
    chk = []
    m = 0
    chk = collections.deque(chk)
    for i in range(n)[::-1]:
      m = (int(s[i])*pow(10,n-1-i,p)+m)%p
      chk.append(m)
    chk.append(0)
    chk = list(chk)
    c = collections.Counter(chk)
    for i in range(p):
      ans += c[i]*(c[i]-1)/2
    print(int(ans))
if __name__ == '__main__':
    main()