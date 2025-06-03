n = int(input())
res = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for _ in range(n):
    seq = input()
    res[seq] += 1

for key in  res.keys():
    print(f"{key} x {res[key]}")