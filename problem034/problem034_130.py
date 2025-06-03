ptn=["23542","14631",
"12651","15621",
"13641","32453"]

def rNO(d):
  global ptn
  for i,e in enumerate(ptn):
    if d in e:
      return i
  return 0
      

dice = list(input().split(" "))
n = int(input())

for i in range(n):
  q = input().split()
  for i,e in enumerate(dice):
    if e == q[0] :
      q1 = i + 1
    if e == q[1]:
      q2 = i + 1
  
  qq=str(q1) + str(q2)
  ans = rNO(qq)
  print(dice[ans])
