A,B,C,D = map(int,input().split())
#高橋体力A 高橋攻撃B
#青木体力C 青木攻撃D
result = "No"
turn = "t"
while 1:
  if turn == "t":
    C -= B
    turn = "a"
    if C <= 0:
      result = "Yes"
      break
  elif turn == "a":
    A -= D
    turn = "t"
    if A <= 0:
      result = "No"
      break
print(result)