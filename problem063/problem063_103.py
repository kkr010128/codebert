import sys

sentence = sys.stdin.read().lower()
alf=[chr(i) for i in range(ord('a'), ord('z')+1)]

ans=dict(zip(alf, [0]*26))

for a in sentence:
  if a in ans:
    ans[a] += 1

for (key, val) in sorted(ans.items()):
  print(key ,":" , val)