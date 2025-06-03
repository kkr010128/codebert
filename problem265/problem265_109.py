# ####################################################################
# import io
# import sys

# _INPUT = """\
# 1001
# 1079
# 432

# 12 5 2
# cabbabaacaba

# 10 2 3
# abccabaabb
# """
# sys.stdin = io.StringIO(_INPUT)
####################################################################
import sys
def p(*_a):
  return
  _s=" ".join(map(str,_a))
  #print(_s)
  sys.stderr.write(_s+"\n")
####################################################################
yn = lambda b: print('Yes') if b else print('No')
####################################################################
N = int(input())

NO = ":("

a = (N-1) // 1.08

for i in range(100):
  b = a + i
  if int(b * 1.08) == N:
    print( int(b) )
    exit()

print(NO)
