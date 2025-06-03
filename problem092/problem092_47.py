x, k, d = map(int, input().split())
cur = x
numTimes = x // d
if numTimes == 0:
    cur -= d
    k -= 1
else:
    numTimes = min(abs(numTimes), k)
    if x < 0:
        numTimes *= -1
    cur -= numTimes * d
    k -= numTimes
if k % 2 == 0:
    print(abs(cur))
else:
    result = min(abs(cur - d), abs(cur + d))
    print(result)