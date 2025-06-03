n = int(input())
s = [input() for _ in range(n)]
dic = {"AC": 0, "WA": 0, "TLE": 0, "RE":0}

for v in s:
  dic[v] += 1

print("AC x {}".format(dic["AC"]))
print("WA x {}".format(dic["WA"]))
print("TLE x {}".format(dic["TLE"]))
print("RE x {}".format(dic["RE"]))
