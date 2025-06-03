n = int(input())
dic = {"AC":0, "WA":0, "TLE":0, "RE":0}
for i in range(n):
  s = input()
  dic[s] += 1
print("AC x " + str(dic["AC"]))
print("WA x " + str(dic["WA"]))
print("TLE x " + str(dic["TLE"]))
print("RE x " + str(dic["RE"]))