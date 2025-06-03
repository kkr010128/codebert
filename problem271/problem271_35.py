N=int(input())
S=input()

ans=""
for x in S:
  if ord("Z")<ord(x)+N:
    ans+=chr(ord(x)+N-26)
  else:
    ans+=chr(ord(x)+N)

print(ans)
