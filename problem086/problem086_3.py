x, y, z = map(int, input().split())

createNum = 0
createTime = 0

loopCnt = x//y
createNum = y*loopCnt
createTime = z*loopCnt

remain = x%y
if remain != 0:
  createTime += z

print(createTime)