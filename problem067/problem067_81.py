num = int(input())

tscore, hscore = 0, 0
for i in range(num):
    ts, hs = input().split()
    if ts > hs:
        tscore += 3
    elif ts < hs:
        hscore += 3
    else:
        tscore += 1
        hscore += 1
print(tscore, hscore)

