n = int(input())
cnt = []
for i in range(n):
    s = input()
    cnt.append(s)
print("AC x ", cnt.count('AC'))
print("WA x ", cnt.count("WA"))
print("TLE x ", cnt.count("TLE"))
print("RE x ", cnt.count("RE"))
