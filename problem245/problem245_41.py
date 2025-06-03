t = input()
al = input()
count = 0
for i in range(len(al)):
  if al[i:].startswith('ABC'):
    count += 1
print(count)