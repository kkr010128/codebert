import sys
A, B = [int(x) for x in input().split()]

ans_A = 0
ans_B = 0
for i in range(1500):
  ans_A = (i*8//100)
  ans_B = (i//10)
  if(ans_A==A)and(ans_B==B):
    print(i)
    sys.exit()
print(-1)