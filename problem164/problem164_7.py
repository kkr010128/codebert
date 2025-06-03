S=list(map(int,input().split()))
while True:
  S[2]=S[2]-S[1]
  S[0]=S[0]-S[3]
  if S[2]<=0:
    print("Yes")
    break
  elif S[0]<=0:
    print("No")
    break