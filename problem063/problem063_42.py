import sys

alphabets = range(ord('a'), ord('z') + 1)
dic = { chr(c): 0 for c in alphabets }

text = sys.stdin.read()
for c in text:
  c = c.lower()
  if ord(c) in alphabets:
    dic[c] += 1

for c, n in sorted(dic.items()):
  print(c, ":", n)