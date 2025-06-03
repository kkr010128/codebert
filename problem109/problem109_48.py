N=int(input())
S=[input() for _ in range(N)]

a=0
w=0
t=0
r=0

for i in range(N):
  if S[i] =="AC":
    a+=1
  elif S[i] =="WA":
    w+=1
  elif S[i] =="TLE":
    t+=1
  elif S[i] =="RE":
    r+=1

print("AC x "+ str(a))
print("WA x "+ str(w))
print("TLE x "+ str(t))
print("RE x "+ str(r))
