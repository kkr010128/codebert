s = input()
q = int(input())
for _ in range(q):
    query = list(input().split())
    l,r = map(int,query[1:3])
    if query[0] == 'replace':
      p = query[3]
      s = s[:l] + p + s[r+1:]
    elif query[0] == 'reverse':
      s = s[:l] + ''.join(list(reversed(s[l:r+1]))) + s[r+1:]
    else:
      print(s[l:r+1])
