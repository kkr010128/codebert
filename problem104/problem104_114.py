A,B,C = map(int,input().split())

L = [i for i in range(A,B + 1)]
_ = 0
for l in L:
  if l % C == 0:
  	_ += 1
print(_)
