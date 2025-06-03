from sys import stdin
n = int(stdin.readline())
c = stdin.readline()[:-1]

red = c.count("R")
ans = red
numwhite = 0
for i in range(n):
    numwhite += 1 if c[i] == "W" else 0
    numred = i - numwhite + 1
    resred = red - numred
    ans = min(ans,max(resred,numwhite))
print(ans)