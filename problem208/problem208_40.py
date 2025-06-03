n, m = map(int, input().split())
d = {"1": -1, "2": -1, "3": -1}
for _ in range(m):
    s, c = input().split()
    if d[s] == -1:
        d[s] = int(c)
    elif d[s] != int(c):
        print(-1)
        exit()
n = str(4 - n)
if n != "3" and d["1"] == 0:
    print(-1)
elif n == "1":
    if d["1"] == -1:
        d["1"] = 1
    if d["2"] == -1:
        d["2"] = 0
    if d["3"] == -1:
        d["3"] = 0
    print(*d.values(), sep="")
elif n == "2":
    if d["1"] == -1:
        d["1"] = 1
    if d["2"] == -1:
        d["2"] = 0
    print(d["1"] * 10 + d["2"])
else:
    if d["1"] == -1:
        d["1"] = 0
    print(d["1"])