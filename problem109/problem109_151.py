import sys; input = sys.stdin.readline
n = int(input())
ac, wa, tle, re = 0, 0, 0, 0
for i in range(n):
    a = input().strip()
    if a == 'AC': ac+=1
    elif a == 'WA': wa += 1
    elif a == 'TLE': tle += 1
    elif a == 'RE': re += 1
print(f"AC x {ac}")
print(f"WA x {wa}")
print(f"TLE x {tle}")
print(f"RE x {re}")