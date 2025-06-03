import sys
  
for line in sys.stdin:
  a,op,b=line.split()
  if op == '?':
    break
  print eval(line)