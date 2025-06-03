N = int(input())

ans = 0

c = input()
redNum = c.count("R")
leftWhite = c.count("W", 0,redNum)
rightRed = c.count("R", redNum,N)

ans += min(leftWhite, rightRed)
if leftWhite > rightRed:
    ans += (leftWhite - rightRed)

print(ans)