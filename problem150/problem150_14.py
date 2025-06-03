N, K = map(int, input().split())
portals = [0] + list(map(int, input().split()))

visitTowns = list()
visitTimes = [0 for _ in range(N + 1)]

curTown = 1
timeBackTo = 0

curTime = 0
while True:
    if visitTimes[curTown] > 0:
        timeBackTo = visitTimes[curTown]
        break

    visitTowns.append(curTown)
    visitTimes[curTown] = curTime

    # teleport
    curTown = portals[curTown]

    curTime += 1

nonLoopCount = timeBackTo
loopSpan = len(visitTowns) - nonLoopCount

if K <= nonLoopCount:
    print(visitTowns[K])
    exit()

rem = (K - nonLoopCount) % loopSpan
print(visitTowns[nonLoopCount + rem])
