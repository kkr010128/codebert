K = int(input())
A, B = map(int, input().split())
cnt = 0
while 1:
  cnt+=K
  if A <= cnt <= B:
    print("OK")
    break
  if B < cnt:
    print("NG")
    break