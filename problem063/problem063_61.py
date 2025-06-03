import string

alphabets = {k:0 for k in string.ascii_lowercase}

while True:
  try:
    for c in input().lower():
      if alphabets.get(c) is None:
        continue
      alphabets[c] += 1
  except:
    break
for c, n in sorted(alphabets.items()):
  print("{} : {}".format(c, n))