n = int(input())
result = [input() for i in range(n)]

print('AC x ' + str(result.count("AC")))
print('WA x ' + str(result.count("WA")))
print('TLE x ' + str(result.count("TLE")))
print('RE x ' + str(result.count("RE")))