n = int(input())
A = [input() for _ in range(n)]

print("AC x " + str(A.count("AC")))
print("WA x " + str(A.count("WA")))
print("TLE x " + str(A.count("TLE")))
print("RE x " + str(A.count("RE")))
