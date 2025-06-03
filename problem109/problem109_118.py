N = int(input())
judge = []
for i in range(N):
    judge.append(input())

counter = [0, 0, 0, 0]
for i in range(N):
    if judge[i] == "AC":
        counter[0] += 1
    if judge[i] == "WA":
        counter[1] += 1
    if judge[i] == "TLE":
        counter[2] += 1
    if judge[i] == "RE":
        counter[3] += 1

print("AC x " + str(counter[0]))
print("WA x " + str(counter[1]))
print("TLE x " + str(counter[2]))
print("RE x " + str(counter[3]))