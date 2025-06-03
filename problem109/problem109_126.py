n = int(input())
strs = []
for _ in range(n):
    strs.append(input())
print("AC x ", strs.count("AC"))
print("WA x ", strs.count("WA"))
print("TLE x ", strs.count("TLE"))
print("RE x ", strs.count("RE"))