def main():
  S = input()
  Q = int(input())
  Query=[input().split() for q in range(Q)]
  cnt=0
  prefix, suffix = '', ''
  for q in Query:
    if q[0]=='1':
      cnt=1^cnt
      prefix, suffix = suffix, prefix
      #print(cnt)
    else:
      if q[1]=='1':
        prefix=prefix+q[2]
      else:
        suffix=suffix+q[2]
  if cnt:
    S=S[::-1]
  print(prefix[::-1]+S+suffix)

main()