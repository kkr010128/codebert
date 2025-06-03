n = int(input())

num_AC = 0
num_WA = 0
num_TLE = 0
num_RE = 0

for i in range(n):
    i = input()
    if i == "AC":
        num_AC += 1
    elif i == "WA":
        num_WA += 1
    elif i == "TLE":
        num_TLE += 1
    elif i == "RE":
        num_RE += 1
    

print("AC x " + str(num_AC))
print("WA x " + str(num_WA))
print("TLE x " + str(num_TLE))
print("RE x " + str(num_RE))