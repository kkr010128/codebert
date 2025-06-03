X = int(input())
ASSET = 100
cnt = 0

while ASSET < X:
  ASSET += ASSET // 100
  cnt += 1

print(cnt)