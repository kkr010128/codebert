n, m = map(int, input().split())
alst = list(map(int, input().split()))
alst.sort(reverse = True)
stand = sum(alst) / m / 4
if alst[m - 1] >= stand:
    print("Yes")
else:
    print("No")