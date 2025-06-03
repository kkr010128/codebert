import sys
def m():
 d={};input()
 for e in sys.stdin:
  if'f'==e[0]:print('yes'if e[5:]in d else'no')
  else:d[e[7:]]=0
if'__main__'==__name__:m()
