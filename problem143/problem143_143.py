k = int (input())
s = input()
line = []

if (len(s) > k):
  for i in range(k):
    line.append(s[i])
  print (''.join(line) + "...")
else:
  print(s)