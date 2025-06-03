X, Y, A ,B, C = list(map(int, input().split()))
P = sorted(list(map(int, input().split())), reverse = True)[:X]
Q = sorted(list(map(int, input().split())), reverse = True)[:Y]
R = sorted(list(map(int, input().split())), reverse = True)
ans = 0
for i in range(C):
  if(len(P) == 0):
    if(len(Q) == 0):
      break
    elif(Q[-1] < R[i]):
      Q.pop()
      ans += R[i]
    else:
      break
  elif(len(Q) == 0):
    if(P[-1] < R[i]):
      P.pop()
      ans += R[i]
    else:
      break
  else:
    if(P[-1] < Q[-1] and P[-1] < R[i]):
      P.pop()
      ans += R[i]
    elif(Q[-1] <= P[-1] and Q[-1] < R[i]):
      Q.pop()
      ans += R[i]
    else:
      break
ans += sum(P) + sum(Q)
print(ans)