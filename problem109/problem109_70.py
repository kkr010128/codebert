N = int(input())
n = 1
S = []
while n <= N:
    s = str(input())
    S.append(s)
    n += 1

print("AC x", S.count("AC"))
print("WA x", S.count("WA"))
print("TLE x", S.count("TLE"))
print("RE x", S.count("RE"))